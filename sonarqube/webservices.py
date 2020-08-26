#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.config import (
    API_WEBSERVICES_LIST_ENDPOINT
)


class SonarQubeWebservices:
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def list_web_services(self, include_internals="false"):
        """
        List web services
        :param include_internals: Include web services that are implemented for internal use only.
        Their forward-compatibility is not assured
        :return:
        """
        params = {'include_internals': include_internals}

        resp = self.sonarqube.make_call('get', API_WEBSERVICES_LIST_ENDPOINT, **params)
        response = resp.json()
        return response['webServices']
