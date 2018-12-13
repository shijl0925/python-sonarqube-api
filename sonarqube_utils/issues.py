#!/usr/bin/env python
# -*- coding:utf-8 -*-
from .config import *


class SonarQubeIssue(object):
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def get_project_issues_page(self,project_key,build_branch,page,resolutions=None,assign_status=None,statuses=None,sinceLeakPeriod=None):
        """
        按页获取issues
        :param project_key:
        :param build_branch:
        :param page:
        :param resolutions:
        :param assign_status:
        :param statuses:
        :param sinceLeakPeriod:
        :return:
        """
        params = {
            'p': page,
            'componentKeys': project_key,
            'branch': build_branch
        }
        if resolutions:
            params['resolutions'] = resolutions
        if assign_status:
            params['assigned'] = assign_status
        if statuses:
            params['statuses'] = statuses
        if sinceLeakPeriod:
            params['sinceLeakPeriod'] = sinceLeakPeriod

        resp = self.sonarqube._make_call('get',RULES_ISSUES_SEARCH_ENDPOINT,**params)
        data = resp.json()
        return data

    def get_project_issues(self,project_key,build_branch,resolutions=None,assign_status=None,statuses=None,sinceLeakPeriod=None):
        """
        获取指定项目的issues
        :param project_key:
        :param build_branch:
        :param resolutions:
        :param assign_status:
        :param statuses:
        :param sinceLeakPeriod:
        :return:
        """
        response = self.get_project_issues_page(project_key,build_branch,1,resolutions,assign_status,statuses,sinceLeakPeriod)
        issues = []

        total_nums = response['paging']['total']
        page_size = response['paging']['pageSize']
        pages = total_nums // page_size + 1
        for i in range(pages):
            response = self.get_project_issues_page(project_key,build_branch,i + 1,resolutions,assign_status,statuses,sinceLeakPeriod)
            issues.extend(response['issues'])
        return issues

    def issue_assign(self,issue_keys,assignee):
        """
        分配issue
        :param issue_keys:
        :param assignee:
        :return:
        """
        params = {
            'assignee': assignee
        }
        if isinstance(issue_keys,list):
            for issue_key in issue_keys:
                params['issue'] = issue_key
                self.sonarqube._make_call('post', RULES_ISSUES_ASSIGN_ENDPOINT, **params)
        elif isinstance(issue_keys,str):
            params['issue'] = issue_keys
            self.sonarqube._make_call('post', RULES_ISSUES_ASSIGN_ENDPOINT, **params)

    def project_issues_do_transition(self,issue_keys,transition):
        """
        对指定项目的issues进行操作
        :param issue_keys:
        :param transition:
        :return:
        """
        params = {
            'transition': transition
        }
        if isinstance(issue_keys,list):
            for issue_key in issue_keys:
                params['issue'] = issue_key
                self.sonarqube._make_call('post', RULES_ISSUES_DO_TRANSITION_ENDPOINT, **params)
        elif isinstance(issue_keys,str):
            params['issue'] = issue_keys
            self.sonarqube._make_call('post', RULES_ISSUES_DO_TRANSITION_ENDPOINT, **params)

