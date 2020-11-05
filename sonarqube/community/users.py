#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_USERS_SEARCH_ENDPOINT,
    API_USERS_CREATE_ENDPOINT,
    API_USERS_UPDATE_ENDPOINT,
    API_USERS_CHANGE_PASSWORD_ENDPOINT,
    API_USERS_GROUPS_ENDPOINT,
    API_USERS_DEACTIVATE_ENDPOINT,
    API_USERS_UPDATE_LOGIN_ENDPOINT,
)
from sonarqube.utils.common import PAGE_GET, POST


class SonarQubeUsers(RestClient):
    """
    SonarQube users Operations
    """

    MAX_SEARCH_NUM = 200

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeUsers, self).__init__(**kwargs)

    def get(self, login):
        """
        Return a list of a given username.

        Args:
            self: (todo): write your description
            login: (int): write your description
        """
        result = list(self.search_users(q=login))
        for user in result:
            if user["login"] == login:
                return user

    @PAGE_GET(API_USERS_SEARCH_ENDPOINT, item="users")
    def search_users(self, q=None):
        """
        Get a list of active users.

        :param q: Filter on login, name and email
        :return:
        """

    def create_user(
        self, login, name, email=None, password=None, local="true", scmAccount=None
    ):
        """
        Create a user.

        :param login: User login
        :param name: User name
        :param email: User email
        :param password: User password. Only mandatory when creating local user, otherwise it should not be set
        :param local: Specify if the user should be authenticated from SonarQube server or from an external
          authentication system. Password should not be set when local is set to false.
          Possible values are for: true, false, yes, no. default value is true.
        :param scmAccount: List of SCM accounts. To set several values, the parameter must be called once for each value.
        :return: request response
        """
        params = {"login": login, "name": name, "local": local}
        if email:
            params.update({"email": email})

        if local == "true" and password:
            params.update({"password": password})

        if scmAccount:
            params.update({"scmAccount": scmAccount})

        return self._post(API_USERS_CREATE_ENDPOINT, params=params)

    @POST(API_USERS_UPDATE_ENDPOINT)
    def update_user(self, login, name=None, email=None, scmAccount=None):
        """
        Update a user.

        :param login: User login
        :param name: User name
        :param email: User email
        :param scmAccount: SCM accounts.
        :return: request response
        """

    @POST(API_USERS_CHANGE_PASSWORD_ENDPOINT)
    def change_user_password(self, login, password, previousPassword=None):
        """
        Update a user's password. Authenticated users can change their own password,
        provided that the account is not linked to an external authentication system.
        Administer System permission is required to change another user's password.

        :param login: User login
        :param password: New password
        :param previousPassword: Previous password. Required when changing one's own password.
        :return:
        """

    @POST(API_USERS_DEACTIVATE_ENDPOINT)
    def deactivate_user(self, login):
        """
        Deactivate a user.

        :param login: User login
        :return: request response
        """

    @PAGE_GET(API_USERS_GROUPS_ENDPOINT, item="groups")
    def search_groups_user_belongs_to(self, login, q=None, selected="selected"):
        """
        Lists the groups a user belongs to.

        :param login:
        :param q: Limit search to group names that contain the supplied string.
        :param selected: Depending on the value, show only selected items (selected=selected), deselected items
          (selected=deselected), or all items with their selection status (selected=all).Possible values are for:
            * all
            * deselected
            * selected
          default value is selected.
        :return:
        """

    @POST(API_USERS_UPDATE_LOGIN_ENDPOINT)
    def update_user_login(self, login, newLogin):
        """
        Update a user login. A login can be updated many times.

        :param login: The current login (case-sensitive)
        :param newLogin: The new login. It must not already exist.
        :return:
        """
