#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_PROJECT_PULL_REQUESTS_DELETE_ENDPOINT,
    API_PROJECT_PULL_REQUESTS_LIST_ENDPOINT,
)
from sonarqube.utils.common import GET, POST


class SonarQubeProjectPullRequests(RestClient):
    """
    SonarQube project pull requests Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeProjectPullRequests, self).__init__(**kwargs)

    @GET(API_PROJECT_PULL_REQUESTS_LIST_ENDPOINT)
    def search_project_pull_requests(self, project):
        """
        SINCE 7.1
        List the pull requests of a project.

        :param project: Project key
        :return:
        """

    @POST(API_PROJECT_PULL_REQUESTS_DELETE_ENDPOINT)
    def delete_project_pull_requests(self, project, pullRequest):
        """
        SINCE 7.1
        Delete a pull request.

        :param project: Project key
        :param pullRequest: Pull request id
        :return:
        """
