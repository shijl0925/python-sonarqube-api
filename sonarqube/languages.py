#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.rest_client import RestClient
from sonarqube.config import API_LANGUAGES_LIST_ENDPOINT


class SonarQubeLanguages(RestClient):
    """
    SonarQube languages Operations
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeLanguages, self).__init__(**kwargs)

    def get_supported_programming_languages(self, q=None):
        """
        List supported programming languages

        :param q: A pattern to match language keys/names against
        :return:
        """
        params = {}
        if q:
            params.update({'q': q})

        resp = self.get(API_LANGUAGES_LIST_ENDPOINT, params=params)
        return resp.json()
