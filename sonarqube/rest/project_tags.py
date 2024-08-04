#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_PROJECT_TAGS_SEARCH_ENDPOINT,
)
from sonarqube.utils.common import GET


class SonarQubeProjectTags(RestClient):
    """
    SonarQube project tags Operations
    """

    @GET(API_PROJECT_TAGS_SEARCH_ENDPOINT)
    def search_project_tags(self, q=None, ps=None, p=None):
        """
        SINCE 6.4
        Search tags

        :param q: Limit search to tags that contain the supplied string.
        :param p: page number.
        :param ps: Page size. Must be greater than 0 and less or equal than 100
        :return:
        """
