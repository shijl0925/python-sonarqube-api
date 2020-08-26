#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.config import (
    API_PROJECT_BRANCHES_LIST_ENDPOINT,
    API_PROJECT_BRANCHES_DELETE_ENDPOINT,
    API_PROJECT_BRANCHES_RENAME_ENDPOINT
)


class SonarQubeProjectBranches:
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def search_project_branches(self, project):
        """
        List the branches of a project.
        :param project: Project key
        :return:
        """
        params = {
            'project': project
        }
        resp = self.sonarqube.make_call('get', API_PROJECT_BRANCHES_LIST_ENDPOINT, **params)
        response = resp.json()
        return response['branches']

    def delete_project_branch(self, project, branch):
        """
        Delete a non-main branch of a project.
        :param project: Project key
        :param branch: Name of the branch
        :return:
        """
        params = {
            'project': project,
            'branch': branch
        }
        self.sonarqube.make_call('post', API_PROJECT_BRANCHES_DELETE_ENDPOINT, **params)

    def rename_project_branch(self, project, name):
        """
        Rename the main branch of a project
        :param project: Project key
        :param name: New name of the main branch
        :return:
        """
        params = {
            'project': project,
            'name': name
        }
        self.sonarqube.make_call('post', API_PROJECT_BRANCHES_RENAME_ENDPOINT, **params)
