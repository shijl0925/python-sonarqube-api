#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.config import (
    API_PROJECT_TAGS_SEARCH_ENDPOINT,
    API_PROJECT_TAGS_SET_ENDPOINT
)


class SonarQubeProjectTags:
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def list_project_tags(self, **kwargs):
        """
        Search tags
        :param kwargs:
        ps: Page size. Must be greater than 0 and less or equal than 100, default value is 10
        q: Limit search to tags that contain the supplied string.
        :return:
        """
        resp = self.sonarqube.make_call('get', API_PROJECT_TAGS_SEARCH_ENDPOINT, **kwargs)
        return resp.json()

    def set_project_tags(self, project, tags):
        """
        Set tags on a project.
        :param project: Project key
        :param tags: Comma-separated list of tags.such as: finance, offshore
        :return:
        """
        params = {
            'project': project,
            'tags': tags
        }
        self.sonarqube.make_call('post', API_PROJECT_TAGS_SET_ENDPOINT, **params)
