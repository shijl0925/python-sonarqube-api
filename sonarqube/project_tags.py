#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.rest_client import RestClient
from sonarqube.config import (
    API_PROJECT_TAGS_SEARCH_ENDPOINT,
    API_PROJECT_TAGS_SET_ENDPOINT
)


class SonarQubeProjectTags(RestClient):
    """
    SonarQube project tags Operations
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeProjectTags, self).__init__(**kwargs)

    def search_project_tags(self, q=None):
        """
        Search tags

        :param q: Limit search to tags that contain the supplied string.
        :return:
        """
        params = {}
        if q:
            params.update({'q': q})

        resp = self.get(API_PROJECT_TAGS_SEARCH_ENDPOINT, params=params)
        return resp.json()

    def set_project_tags(self, project, tags):
        """
        Set tags on a project.

        :param project: Project key
        :param tags: Comma-separated list of tags.Possible values are for: finance, offshore
        :return:
        """
        params = {
            'project': project,
            'tags': tags
        }

        self.post(API_PROJECT_TAGS_SET_ENDPOINT, params=params)
