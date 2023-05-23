#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_AUTH_LOGIN_ENDPOINT,
    API_AUTH_LOGOUT_ENDPOINT,
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

    @POST(API_AUTH_LOGIN_ENDPOINT)
    def authenticate_user(self, login, password):
        """
        SINCE 6.0
        Authenticate a user.

        :param login: Login of the user
        :param password: Password of the user
        :return:
        """

    @POST(API_AUTH_LOGOUT_ENDPOINT)
    def logout_user(self):
        """
        SINCE 6.3
        Logout a user.

        :return:
        """

    @GET(API_AUTH_VALIDATE_ENDPOINT)
    def check_credentials(self):
        """
        SINCE 3.3
        Check credentials.

        :return:
        """
