#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_USERS_SEARCH_ENDPOINT,
)
from sonarqube.utils.common import GET


class SonarQubeUsers(RestClient):
    """
    SonarQube users Operations
    """

    def get_user(self, login):
        result = self.search_users(q=login)
        users = result.get("users", [])
        item = None
        for user in users:
            if user["login"] == login:
                item = user
                break

        return item

    @GET(API_USERS_SEARCH_ENDPOINT)
    def search_users(self, q=None, p=None, ps=None):
        """
        SINCE 3.6
        Get a list of active users.

        :param q: Filter on login, name and email
        :param p: page number.
        :param ps: Page size. Must be greater than 0 and less or equal than 500
        :return:
        """
