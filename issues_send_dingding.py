#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os
from sonarqube_utils.base_api import SonarAPIHandler
from utils.common import get_json_data
from generateReport import generate_issues_dingding_report
import time
from dingtalk import SecretClient
from fuzzywuzzy import fuzz
from dingtalk.model.message import MarkdownBody
from dingtalk_group_members import get_dingtalk_members
from collections import defaultdict

try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass

def fuzzy_search_author(author, users):
    """
    模糊搜索分配人
    :param author:
    :return:
    """
    compare_result = {}
    for user in users:
        compare_result[user] = fuzz.ratio(author, user)

    result = sorted(compare_result.items(), key=lambda x: x[1], reverse=True)
    if result[0][1] > 90:
        return result[0][0]

def get_assign_issues(sonarhandler, running_job, build_branch, assigned='true', statuses='OPEN,CONFIRMED,REOPENED', sinceLeakPeriod='false'):
    """
    获取分配的issues
    :param sonarhandler:
    :param running_job:
    :param build_branch:
    :param assigned:
    :param statuses:
    :param sinceLeakPeriod:
    :return:
    """
    sonarqube_users_info = {item['login']: item for item in sonarhandler.users}

    issues = sonarhandler.issues.get_project_issues(running_job, build_branch, assigned=assigned, statuses=statuses, sinceLeakPeriod=sinceLeakPeriod)
    assign_issues = defaultdict(list)
    for issue in issues:
        if 'assignee' in issue and issue['assignee'] in sonarqube_users_info:
            assignee_email = sonarqube_users_info[issue['assignee']]['email']
            assign_issues[assignee_email].append(issue)
    return assign_issues

def assign_unassigned_issues(sonarhandler, running_job, build_branch):
    """
    获取未分配的issues，然后进行分配
    :param sonarhandler
    :param running_job:
    :param build_branch:
    :return:
    """
    sonarqube_users_info = {item['login']: item for item in sonarhandler.users}

    issues = sonarhandler.issues.get_project_issues(running_job, build_branch, assigned='false', statuses='OPEN,CONFIRMED,REOPENED', sinceLeakPeriod='false')
    for issue in issues:
        assignee = issue['author'].split('@')[0]
        issue_key = str(issue['key'])

        if assignee in sonarqube_users_info:
            sonarhandler.issues.issue_assign(issue_key, assignee)
            print('Assign issue {} to {}'.format(issue_key, assignee))
        else:
            result = fuzzy_search_author(assignee, list(sonarqube_users_info.keys()))
            if result:
                sonarhandler.issues.issue_assign(issue_key,result)
                print('Assign issue {} to fuzzy author {}'.format(issue_key,result))

if __name__ == "__main__":
    running_job = sys.argv[1]
    build_branch = sys.argv[2]

    script_path = os.path.split(os.path.realpath(__file__))[0]
    config = get_json_data(os.path.join(script_path, 'config', 'config.json'))
    sonarqube_config = config['sonarqube_config']

    try:
        sonarhandler = SonarAPIHandler(sonarqube_config['sonarqube_direct_url'],
                                       sonarqube_config['sonar_user'],
                                       sonarqube_config['sonar_password'])
        print('{} connect successful.'.format(sonarhandler._sonarqube_url))
    except Exception as err:
        print(err)
        sys.exit(1)

    dingtalk_config = config['dingtalk_config']
    CorpId = dingtalk_config['CorpId']
    CorpSecret = dingtalk_config['CorpSecret']
    agentid = dingtalk_config['agentid']

    dingtalk_client = SecretClient(CorpId, CorpSecret)

    # 获取研发中心成员信息
    dev_members_info = {item[0]: {'name': item[1], 'userid':item[2]} for item in get_dingtalk_members()}

    title = u'[SonarQube]代码静态分析报告'

    project_id = sonarhandler.projects.get_project_id(running_job)
    while len(sonarhandler.ce.get_project_activity_status(project_id, 'IN_PROGRESS')) == 1:
        time.sleep(1)
        print('waiting for sonarqube project {}...'.format(running_job))
    else:
        time.sleep(5)

        # 获取未分配的issues，然后进行分配
        assign_unassigned_issues(sonarhandler, running_job, build_branch)

        # 获取measures内容
        measures_component = sonarhandler.measures.get_project_measures_component(running_job, build_branch)

        # 获取所有分配好的issus
        assign_issues = get_assign_issues(sonarhandler, running_job, build_branch)

        # 获取状态为'OPEN,REOPENED'的分配好的issues
        opened_reopened_assign_issues = get_assign_issues(sonarhandler, running_job, build_branch, statuses='OPEN,REOPENED')

        # 给分配人发送报告
        for a, issues in assign_issues.items():
            if dev_members_info and a in dev_members_info:
                # 生成钉钉通知
                issues_report = generate_issues_dingding_report(measures_component, issues, running_job, build_branch)
                msg_body = MarkdownBody(title, issues_report)
                user_id = dev_members_info[a]['userid']
                user_name = dev_members_info[a]['name']
                touser_list = [user_id]

                dingtalk_client.message.send(agentid, msg_body, touser_list=touser_list, toparty_list=[])
                print('Send issues dingding Report to %s successful.' % user_name)

            # 将未确认的issue的状态置为confirmed
            if opened_reopened_assign_issues and a in opened_reopened_assign_issues:
                issues = opened_reopened_assign_issues[a]
                issue_keys = [issue['key'] for issue in issues]
                sonarhandler.issues.project_issues_do_transition(issue_keys, transition='confirm')
                print('Set issues {} confirmed successful.'.format(issue_keys))

