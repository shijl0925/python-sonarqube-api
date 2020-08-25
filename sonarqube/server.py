#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.config import API_SERVER_VERSION_ENDPOINT


class SonarQubeServer:
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def get_server_version(self):
        """
        Version of SonarQube in plain text
        :return:
        """
        resp = self.sonarqube.make_call('get', API_SERVER_VERSION_ENDPOINT)
        return resp.text