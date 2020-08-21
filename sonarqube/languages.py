#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.config import API_LANGUAGES_LIST_ENDPOINT


class SonarQubeLanguages:
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def get_languages_list(self, **kwargs):
        """
        List supported programming languages
        :param kwargs:
        ps: The size of the list to return, 0 for all languages
        q: A pattern to match language keys/names against
        :return:
        """
        resp = self.sonarqube.make_call('get', API_LANGUAGES_LIST_ENDPOINT, **kwargs)
        return resp.json()
