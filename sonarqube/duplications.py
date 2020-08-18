#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sonarqube.config import API_DUPLICATIONS_SHOW_ENDPOINT


class SonarQubeDuplications:
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def get_duplications(self, key):
        """
        Get duplications. Require Browse permission on file's project
        :param key:
        :return:
        """
        params = {'key': key}
        resp = self.sonarqube.make_call('get', API_DUPLICATIONS_SHOW_ENDPOINT, **params)
        data = resp.json()
        return data
