#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_PROJECT_TAGS_SEARCH_ENDPOINT,
    API_PROJECT_TAGS_SET_ENDPOINT,
)
from sonarqube.utils.common import GET, POST


class SonarQubeProjectTags(RestClient):
    """
    SonarQube project tags Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeProjectTags, self).__init__(**kwargs)

    @GET(API_PROJECT_TAGS_SEARCH_ENDPOINT)
    def search_project_tags(self, q=None):
        """
        SINCE 6.4
        Search tags

        :param q: Limit search to tags that contain the supplied string.
        :return:
        """

    @POST(API_PROJECT_TAGS_SET_ENDPOINT)
    def set_project_tags(self, project, tags):
        """
        SINCE 6.4
        Set tags on a project.

        :param project: Project key
        :param tags: Comma-separated list of tags.Possible values are for: finance, offshore
        :return:
        """
