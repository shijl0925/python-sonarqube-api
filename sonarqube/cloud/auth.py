#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_AUTH_LOGOUT_ENDPOINT,
    API_AUTH_VALIDATE_ENDPOINT
)


class SonarCloudAuth(RestClient):
    """
    SonarCloud authentication Operations
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarCloudAuth, self).__init__(**kwargs)

    def logout_user(self):
        """
        Logout a user.

        :return:
        """
        self.post(API_AUTH_LOGOUT_ENDPOINT)

    def check_credentials(self):
        """
        Check credentials.

        :return:
        """
        resp = self.get(API_AUTH_VALIDATE_ENDPOINT)
        return resp.json()
