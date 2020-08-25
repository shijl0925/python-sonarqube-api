#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.config import (
    API_AUTH_LOGIN_ENDPOINT,
    API_AUTH_LOGOUT_ENDPOINT,
    API_AUTH_VALIDATE_ENDPOINT
)


class SonarQubeAuth:
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def authenticate_user(self, login, password):
        """
        Authenticate a user.
        :param login:
        :param password:
        :return:
        """
        params = {
            'login': login,
            'password': password
        }
        self.sonarqube.make_call('post', API_AUTH_LOGIN_ENDPOINT, **params)

    def logout_user(self):
        """
        Logout a user.
        :return:
        """
        self.sonarqube.make_call('post', API_AUTH_LOGOUT_ENDPOINT)

    def check_credentials(self):
        """
        Check credentials.
        :return:
        """
        resp = self.sonarqube.make_call('get', API_AUTH_VALIDATE_ENDPOINT)
        return resp.json()
