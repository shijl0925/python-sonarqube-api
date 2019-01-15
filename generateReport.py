#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import urllib
import sys
from utils.common import get_json_data, today, get_template

try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass

script_path = os.path.split(os.path.realpath(__file__))[0]
config = get_json_data(os.path.join(script_path, 'config', 'config.json'))
sonarqube_url = config['sonarqube_config']['sonarqube_direct_url']

def generate_issues_report(project_name, issues, issue_type):
    """
    :param project_name:
    :param issues:
    :param issue_type:
    :return:
    """
    report = ''
    for issue in issues:
        report = report + generate_issue_string(project_name, issue, issue_type)
    return report

def generate_issue_string(project_name, issue, issue_type):
    """
    :param project_name:
    :param issue:
    :param issue_type:
    :return:
    """
    report = ''
    if issue['type'] == issue_type:
        key = issue['key']
        issues_detail_link = '{}/project/issues?id={}&issues={}'.format(sonarqube_url, project_name,key)
        report = report + '\n>###### More details at: ' + '<a href="{}" >{}</a>'.format(issues_detail_link, issues_detail_link)
    return report

def generate_issue_numbers(issues):
    """
    从issues中计算bug、漏洞、坏味道数量
    :param issues:
    :return:
    """
    bugs_number = 0
    vulnerabilities_number = 0
    smells_number =0

    for issue in issues:
        if issue['type'] == 'BUG':
            bugs_number += 1
        elif issue['type'] == 'VULNERABILITY':
            vulnerabilities_number += 1
        elif issue['type'] == 'CODE_SMELL':
            smells_number += 1

    return bugs_number, vulnerabilities_number, smells_number

def generate_issues_email_report(measures_component, issues, job_name, build_branch):
    """
    生成邮件标题和邮件报告
    :param measures_component:
    :param issues:
    :param job_name:
    :param build_branch:
    :return:
    """
    TEMPLATE = get_template(os.path.join(script_path, 'template', 'issues_email_template.txt'))
    # 发送通知邮件
    subject = '[SONARQUBE]' + job_name + u' 代码静态分析报告 - ' + today
    return subject, generate_template_report(TEMPLATE, measures_component, issues,job_name, build_branch)

def generate_issues_dingding_report(measures_component, issues, job_name, build_branch):
    """
    生成钉钉通知报告
    :param measures_component:
    :param issues:
    :param job_name:
    :param build_branch:
    :return:
    """
    issues_template = u'''
#### [[SonarQube] __project_name__](__sonarqube_project_url__)
&nbsp;

#### **__build_branch__分支代码静态分析结果：**
&nbsp;

##### Bugs __bugs__，  新增：__new_bugs__
##### 漏洞 __vulnerabilities__，  新增：__new_vulnerabilities__
##### 坏味道 __code_smells__，  新增：__new_code_smells__
&nbsp;

#### **分配给我的问题：**
&nbsp;

##### [Bugs: __bugs_num__](__my_bugs_url__) ；  [漏洞: __vulnerabilities_num__](__my_vulnerabilities_url__) ；  [坏味道: __smells_num__](__my_code_smells_url__)
&nbsp;

#### **请登录查看，并及时修复。**

'''
    issues_template = generate_template_report(issues_template, measures_component, issues, job_name, build_branch)
    return issues_template

def generate_template_report(template, measures_component, issues, job_name, build_branch):
    """
    用来处理模板来生成报告
    :param template:
    :param measures_component:
    :param issues:
    :param job_name:
    :param build_branch:
    :return:
    """
    template = template.replace('__sonarqube_url__', sonarqube_url + '/projects?sort=name')
    m = config['metrics'].split(',')

    # 替换template中扫描问题的数值
    for i in m:
        if i in measures_component:
            template = template.replace('__' + i + '__', measures_component[i])
        else:
            template = template.replace('__' + i + '__', str(0))

    # 替换template中分支
    template = template.replace('__build_branch__', build_branch)

    t = (sonarqube_url, job_name, build_branch)
    # 替换template中分析项目的名字和项目地址
    sonarqube_project_url = '{}/dashboard?id={}&branch={}'.format(*t)
    template = template.replace('__project_name__', job_name)

    try:
        url = urllib.quote_plus(sonarqube_project_url)
    except:
        url = urllib.parse.quote_plus(sonarqube_project_url)
    template = template.replace('__sonarqube_project_url__', "{}/sessions/init/gitlab?return_to={}".format(sonarqube_url, url))

    # 替换template中分析时间
    template = template.replace('__date__', today)

    # 替换template中链接到我的bug、漏洞、坏味道的地址
    my_bugs_url = '{}/project/issues?id={}&branch={}&myIssues=true&resolved=false&types=BUG'.format(*t)
    my_vulnerabilities_url = '{}/project/issues?id={}&branch={}&myIssues=true&resolved=false&types=VULNERABILITY'.format(*t)
    my_code_smells_url = '{}/project/issues?id={}&branch={}&myIssues=true&resolved=false&types=CODE_SMELL'.format(*t)

    template = template.replace('__my_bugs_url__', my_bugs_url)
    template = template.replace('__my_vulnerabilities_url__', my_vulnerabilities_url)
    template = template.replace('__my_code_smells_url__', my_code_smells_url)

    # 替换template中链接到我的bug、漏洞、坏味道的数值
    bugs_number, vulnerabilities_number, smells_number = generate_issue_numbers(issues)
    template = template.replace('__bugs_num__', str(bugs_number))
    template = template.replace('__vulnerabilities_num__', str(vulnerabilities_number))
    template = template.replace('__smells_num__', str(smells_number))

    return template
