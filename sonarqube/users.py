#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.config import (
    API_USERS_SEARCH_ENDPOINT,
    API_USERS_CREATE_ENDPOINT,
    API_USERS_UPDATE_ENDPOINT,
    API_USERS_CHANGE_PASSWORD_ENDPOINT,
    API_USERS_GROUPS_ENDPOINT,
    API_USERS_DEACTIVATE_ENDPOINT,
    API_USERS_UPDATE_LOGIN_ENDPOINT
)


class SonarQubeUser:
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube
        self._data = None

    def poll(self):
        self._data = self.search_users()

    def iterkeys(self):
        """

        :return:
        """
        for item in self:
            yield item['login']

    def keys(self):
        """

        :return:
        """
        return list(self.iterkeys())

    def __len__(self):
        """

        :return:
        """
        return len(self.keys())

    def __contains__(self, login_name):
        """

        :param login_name:
        :return:
        """
        result = self.search_users(q=login_name)
        logins = [item['login'] for item in result]
        return login_name in logins

    def __getitem__(self, index):
        """

        :param index:
        :return:
        """
        return list(self)[index]

    def __iter__(self):
        """

        :return:
        """
        self.poll()
        return self._data

    def search_users(self, q=None):
        """
        Get a list of active users.

        :param q: Filter on login, name and email
        :return:
        """
        params = {}
        page_num = 1
        page_size = 1
        total = 2

        if q:
            params.update({'q': q})

        while page_num * page_size < total:
            resp = self.sonarqube.make_call('get', API_USERS_SEARCH_ENDPOINT, **params)
            response = resp.json()

            page_num = response['paging']['pageIndex']
            page_size = response['paging']['pageSize']
            total = response['paging']['total']

            params['p'] = page_num + 1

            for user in response['users']:
                yield user

    def create_user(self, login, name, email=None, password=None, local='true', scm=None):
        """
        Create a user.

        :param login: User login
        :param name: User name
        :param email: User email
        :param password: User password. Only mandatory when creating local user, otherwise it should not be set
        :param local: Specify if the user should be authenticated from SonarQube server or from an external authentication system.
          Password should not be set when local is set to false.
          Possible values are for: true, false, yes, no. default value is true.
        :param scm: List of SCM accounts. To set several values, the parameter must be called once for each value.
        :return: request response
        """
        params = {
            'login': login,
            'name': name,
            'local': local
        }
        if email:
            params.update({'email': email})

        if local == 'true' and password:
            params.update({'password': password})

        if scm:
            params.update({'scmAccount': scm})

        return self.sonarqube.make_call('post', API_USERS_CREATE_ENDPOINT, **params)

    def update_user(self, login, name=None, email=None, scm=None):
        """
        Update a user.

        :param login: User login
        :param name: User name
        :param email: User email
        :param scm: SCM accounts.
        :return: request response
        """
        params = {
            'login': login
        }

        if name:
            params.update({'name': name})

        if email:
            params.update({'email': email})

        if scm:
            params.update({'scmAccount': scm})

        return self.sonarqube.make_call('post', API_USERS_UPDATE_ENDPOINT, **params)

    def change_user_password(self, login, new_password, previous_password=None):
        """
        Update a user's password. Authenticated users can change their own password,
        provided that the account is not linked to an external authentication system.
        Administer System permission is required to change another user's password.

        :param login: User login
        :param new_password: New password
        :param previous_password: Previous password. Required when changing one's own password.
        :return:
        """
        params = {
            'login': login,
            'password': new_password
        }
        if previous_password:
            params.update({'previousPassword': previous_password})

        self.sonarqube.make_call('post', API_USERS_CHANGE_PASSWORD_ENDPOINT, **params)

    def deactivate_user(self, login):
        """
        Deactivate a user.

        :param login: User login
        :return: request response
        """
        params = {
            'login': login
        }
        return self.sonarqube.make_call('post', API_USERS_DEACTIVATE_ENDPOINT, **params)

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
        params = {
            'login': login,
            'selected': selected
        }

        if q:
            params.update({'q': q})

        page_num = 1
        page_size = 1
        total = 2

        if q:
            params.update({'q': q})

        while page_num * page_size < total:
            resp = self.sonarqube.make_call('get', API_USERS_GROUPS_ENDPOINT, **params)
            response = resp.json()

            page_num = response['paging']['pageIndex']
            page_size = response['paging']['pageSize']
            total = response['paging']['total']

            params['p'] = page_num + 1

            for group in response['groups']:
                yield group

    def update_user_login(self, login, new_login):
        """
        Update a user login. A login can be updated many times.

        :param login: The current login (case-sensitive)
        :param new_login: The new login. It must not already exist.
        :return:
        """
        params = {
            'login': login,
            'newLogin': new_login
        }

        self.sonarqube.make_call('post', API_USERS_UPDATE_LOGIN_ENDPOINT, **params)
