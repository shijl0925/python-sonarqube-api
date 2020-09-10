#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.rest_client import RestClient
from sonarqube.config import API_DUPLICATIONS_SHOW_ENDPOINT


class SonarQubeDuplications(RestClient):
    """
    SonarQube duplications Operations
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeDuplications, self).__init__(**kwargs)

    def get_duplications(self, key):
        """
        Get duplications. Require Browse permission on file's project

        :param key: File key
        :return:
        """
        params = {'key': key}

        resp = self.get(API_DUPLICATIONS_SHOW_ENDPOINT, params=params)
        return resp.json()
