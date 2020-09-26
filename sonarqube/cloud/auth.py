#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.community.auth import SonarQubeAuth


class SonarCloudAuth(SonarQubeAuth):
    """
    SonarCloud authentication Operations
    """

    def authenticate_user(self, login, password):
        """
        Authenticate a user.

        :param login: Login of the user
        :param password: Password of the user
        :return:
        """
        raise AttributeError(
            "%s does not support this method" % self.__class__.__name__
        )
