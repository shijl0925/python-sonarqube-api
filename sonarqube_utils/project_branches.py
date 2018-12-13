#!/usr/bin/env python
#-*- coding:utf-8 -*-
from .config import *

class SonarQubeProject_Branches(object):
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def get_project_branches_list(self, project_key):
        """
        显示项目分支
        :param project_key:
        :return:
        """
        params = {
            'project': project_key
        }
        resp = self.sonarqube._make_call('get', RULES_PROJECT_BRANCHES_LIST_ENDPOINT, **params)
        data = resp.json()
        branches = []
        for i in data['branches']:
            branches.append(i['name'])
        return branches

    def delete_project_branch(self, project_key, branch):
        """
        删除项目分支
        :param project_key:
        :param branch:
        :return:
        """
        params = {
            'project': project_key,
            'branch': branch
        }
        self.sonarqube._make_call('get', RULES_PROJECT_BRANCHES_DELETE_ENDPOINT, **params)

    def rename_project_branch(self, project_key, branch):
        """
        Rename the main branch of a project
        :param project_key:
        :param branch:
        :return:
        """
        params = {
            'project': project_key,
            'name': branch
        }
        self.sonarqube._make_call('get', RULES_PROJECT_BRANCHES_RENAME_ENDPOINT, **params)

