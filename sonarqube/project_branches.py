#!/usr/bin/env python
# -*- coding:utf-8 -*-
from .config import *


class SonarQubeProject_Branches(object):
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def get_project_branches_list(self, project):
        """
        List the branches of a project.
        :param project:
        :return:
        """
        params = {
            'project': project
        }
        resp = self.sonarqube._make_call('get', API_PROJECT_BRANCHES_LIST_ENDPOINT, **params)
        data = resp.json()
        return data['branches']

    def delete_project_branch(self, project, branch):
        """
        Delete a non-main branch of a project.
        :param project:
        :param branch:
        :return:
        """
        params = {
            'project': project,
            'branch': branch
        }
        self.sonarqube._make_call('post', API_PROJECT_BRANCHES_DELETE_ENDPOINT, **params)

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
        self.sonarqube._make_call('post', API_PROJECT_BRANCHES_RENAME_ENDPOINT, **params)

