#!/usr/bin/env python
# -*- coding:utf-8 -*-
from .config import *

class SonarQubeComponents(object):
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def components_show(self, component):
        """
        :param component:
        :return:
        """
        params = {
            'component': component
        }

        resp = self.sonarqube._make_call('get', RULES_COMPONTENTS_SHOW_ENDPOINT, **params)
        data = resp.json()
        return data['component']
