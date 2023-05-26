#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_AUTH_VALIDATE_ENDPOINT,
)
from sonarqube.utils.common import GET, POST


class SonarQubeAuth(RestClient):
    """
    SonarQube authentication Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeAuth, self).__init__(**kwargs)

    @GET(API_AUTH_VALIDATE_ENDPOINT)
    def check_credentials(self):
        """
        SINCE 3.3
        Check credentials.

        :return:
        """
