#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import API_USERS_SEARCH_ENDPOINT, API_USERS_GROUPS_ENDPOINT
from sonarqube.utils.common import PAGES_GET


class SonarCloudUsers(RestClient):
    """
    SonarCloud users Operations
    """

    MAX_SEARCH_NUM = 200

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarCloudUsers, self).__init__(**kwargs)

    def get(self, login):
        result = list(self.search_users(q=login))
        for user in result:
            if user["login"] == login:
                return user

    @PAGES_GET(API_USERS_SEARCH_ENDPOINT, item="users")
    def search_users(self, q=None):
        """
        Get a list of active users.

        :param q: Filter on login, name and email
        :return:
        """

    @PAGES_GET(API_USERS_GROUPS_ENDPOINT, item="groups")
    def search_groups_user_belongs_to(
        self, login, organization, q=None, selected="selected"
    ):
        """
        Lists the groups a user belongs to.

        :param login:
        :param organization: organization key.
        :param q: Limit search to group names that contain the supplied string.
        :param selected: Depending on the value, show only selected items (selected=selected), deselected items
          (selected=deselected), or all items with their selection status (selected=all).Possible values are for:
            * all
            * deselected
            * selected
          default value is selected.
        :return:
        """
