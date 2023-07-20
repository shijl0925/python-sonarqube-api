#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_PROJECT_LINKS_SEARCH_ENDPOINT,
)
from sonarqube.utils.common import GET, POST


class SonarQubeProjectLinks(RestClient):
    """
    SonarQube project badges Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeProjectLinks, self).__init__(**kwargs)

    @GET(API_PROJECT_LINKS_SEARCH_ENDPOINT)
    def search_project_links(self, projectId=None, projectKey=None):
        """
        SINCE 6.1
        List links of a project.
        The 'projectId' or 'projectKey' must be provided.

        :param projectId: ProjectId
        :param projectKey: ProjectKey
        :return:
        """
