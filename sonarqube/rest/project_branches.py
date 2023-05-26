#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_PROJECT_BRANCHES_LIST_ENDPOINT,
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