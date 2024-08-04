#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_AUTH_VALIDATE_ENDPOINT,
)
from sonarqube.utils.common import GET


class SonarQubeAuth(RestClient):
    """
    SonarQube authentication Operations
    """

    @GET(API_AUTH_VALIDATE_ENDPOINT)
    def check_credentials(self):
        """
        SINCE 3.3
        Check credentials.

        :return:
        """
