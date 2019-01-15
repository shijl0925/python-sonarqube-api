#!/usr/bin/env python
# -*- coding:utf-8 -*-
from .config import *

class SonarQubeProject_Branches(object):
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def get_project_branches_list(self, project):
        """
        显示项目分支
        :param project:
        :return:
        """
        params = {
            'project': project
        }
        resp = self.sonarqube._make_call('get', RULES_PROJECT_BRANCHES_LIST_ENDPOINT, **params)
        data = resp.json()
        return data['branches']

    def delete_project_branch(self, project, branch):
        """
        删除项目分支
        :param project:
        :param branch:
        :return:
        """
        params = {
            'project': project,
            'branch': branch
        }
        self.sonarqube._make_call('get', RULES_PROJECT_BRANCHES_DELETE_ENDPOINT, **params)

    def rename_project_branch(self, project, name):
        """
        Rename the main branch of a project
        :param project:
        :param name:
        :return:
        """
        params = {
            'project': project,
            'name': name
        }
        self.sonarqube._make_call('get', RULES_PROJECT_BRANCHES_RENAME_ENDPOINT, **params)

