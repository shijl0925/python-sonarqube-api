#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import API_SERVER_VERSION_ENDPOINT
from sonarqube.utils.common import GET


class SonarQubeServer(RestClient):
    """
    SonarQube server Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeServer, self).__init__(**kwargs)

    @GET(API_SERVER_VERSION_ENDPOINT)
    def get_server_version(self):
        """
        SINCE 2.10
        Version of SonarQube in plain text

        :return:
        """
