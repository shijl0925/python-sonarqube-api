#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.config import API_LANGUAGES_LIST_ENDPOINT


class SonarQubeLanguages:
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def get_supported_programming_languages(self, q=None):
        """
        List supported programming languages
        :param q: A pattern to match language keys/names against
        :return:
        """
        params = {}
        if q:
            params.update({'q': q})
        resp = self.sonarqube.make_call('get', API_LANGUAGES_LIST_ENDPOINT, **params)
        return resp.json()
