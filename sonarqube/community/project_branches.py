#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_PROJECT_BRANCHES_LIST_ENDPOINT,
    API_PROJECT_BRANCHES_DELETE_ENDPOINT,
    API_PROJECT_BRANCHES_RENAME_ENDPOINT
)


class SonarQubeProjectBranches(RestClient):
    """
    SonarQube project branches Operations
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeProjectBranches, self).__init__(**kwargs)

    def search_project_branches(self, project):
        """
        List the branches of a project.

        :param project: Project key
        :return:
        """
        params = {
            'project': project
        }

        resp = self.get(API_PROJECT_BRANCHES_LIST_ENDPOINT, params=params)
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

        self.post(API_PROJECT_BRANCHES_DELETE_ENDPOINT, params=params)

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

        self.post(API_PROJECT_BRANCHES_RENAME_ENDPOINT, params=params)
