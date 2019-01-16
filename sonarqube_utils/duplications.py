#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .config import *

class SonarQubeDuplications(object):
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def get_duplications(self, key):
        """
        Get duplications. Require Browse permission on file's project
        :param key:
        :return:
        """
        params = {'key': key}
        resp = self.sonarqube._make_call('get', RULES_DUPLICATIONS_SHOW_ENDPOINT, **params)
        data = resp.json()
        return data