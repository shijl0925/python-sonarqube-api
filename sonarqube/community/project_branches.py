#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_PROJECT_BRANCHES_LIST_ENDPOINT,
    API_PROJECT_BRANCHES_DELETE_ENDPOINT,
    API_PROJECT_BRANCHES_RENAME_ENDPOINT,
    API_PROJECT_BRANCHES_SET_PROTECTION_ENDPOINT,
)
from sonarqube.utils.common import GET, POST


class SonarQubeProjectBranches(RestClient):
    """
    SonarQube project branches Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeProjectBranches, self).__init__(**kwargs)

    @GET(API_PROJECT_BRANCHES_LIST_ENDPOINT)
    def search_project_branches(self, project):
        """
        SINCE 6.6
        List the branches of a project.

        :param project: Project key
        :return:
        """

    @POST(API_PROJECT_BRANCHES_DELETE_ENDPOINT)
    def delete_project_branch(self, project, branch):
        """
        SINCE 6.6
        Delete a non-main branch of a project.

        :param project: Project key
        :param branch: Name of the branch
        :return:
        """

    @POST(API_PROJECT_BRANCHES_RENAME_ENDPOINT)
    def rename_project_branch(self, project, name):
        """
        SINCE 6.6
        Rename the main branch of a project

        :param project: Project key
        :param name: New name of the main branch
        :return:
        """

    @POST(API_PROJECT_BRANCHES_SET_PROTECTION_ENDPOINT)
    def set_automatic_deletion_protection_for_project_branch(self, project, branch, value):
        """
        SINCE 8.1
        Protect a specific branch from automatic deletion. Protection can't be disabled for the main branch.

        :param project: Project key
        :param branch: Branch key
        :param value: Sets whether the branch should be protected from automatic deletion
          when it hasn't been analyzed for a set period of time. Possible values are for: true or false, yes or no.
        :return:
        """