#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.community.user_groups import SonarQubeUserGroups
from sonarqube.utils.config import (
    API_USER_GROUPS_SEARCH_ENDPOINT,
    API_USER_GROUPS_CREATE_ENDPOINT,
    API_USER_GROUPS_DELETE_ENDPOINT,
    API_USER_GROUPS_USERS_ENDPOINT,
    API_USER_GROUPS_ADD_USER_ENDPOINT,
    API_USER_GROUPS_REMOVE_USER_ENDPOINT
)


class SonarCloudUserGroups(SonarQubeUserGroups):
    """
    SonarCloud user_groups Operations
    """
    def __getitem__(self, key):
        raise AttributeError("%s does not support this method" % self.__class__.__name__)

    def search_user_groups(self, organization, fields=None, q=None):
        """
        Search for user groups.

        :param organization: organization key.
        :param fields: Comma-separated list of the fields to be returned in response.
          All the fields are returned by default. Possible values are for:
            * name
            * description
            * membersCount
        :param q: Limit search to names that contain the supplied string.
        :return:
        """
        params = {'organization': organization}

        if fields:
            params.update({"f": fields})

        page_num = 1
        page_size = 1
        total = 2

        if q:
            params['q'] = q

        while page_num * page_size < total:
            resp = self.get(API_USER_GROUPS_SEARCH_ENDPOINT, params=params)
            response = resp.json()

            page_num = response['paging']['pageIndex']
            page_size = response['paging']['pageSize']
            total = response['paging']['total']

            params['p'] = page_num + 1

            for group in response['groups']:
                yield group

    def create_group(self, group_name, organization, description=None):
        """
        Create a group.

        :param group_name: Name for the new group. A group name cannot be larger than 255 characters and must be unique.
          The value 'anyone' (whatever the case) is reserved and cannot be used.
        :param organization: organization key.
        :param description: Description for the new group. A group description cannot be larger than 200 characters.
        :return: request response
        """
        params = {
            'name': group_name,
            'organization': organization
        }
        if description:
            params.update({'description': description})

        return self.post(API_USER_GROUPS_CREATE_ENDPOINT, params=params)

    def delete_group(self, group_name, organization):
        """
        Delete a group. The default groups cannot be deleted.

        :param group_name: group name
        :param organization: organization key.
        :return:
        """
        params = {
            'name': group_name,
            'organization': organization
        }

        self.post(API_USER_GROUPS_DELETE_ENDPOINT, params=params)

    def add_user_to_group(self, group_name, user_login, organization):
        """
        Add a user to a group.

        :param group_name: Group name
        :param user_login: User login
        :param organization: organization key.
        :return:
        """
        params = {
            'login': user_login,
            'name': group_name,
            'organization': organization
        }

        self.post(API_USER_GROUPS_ADD_USER_ENDPOINT, params=params)

    def remove_user_from_group(self, group_name, user_login, organization):
        """
        Remove a user from a group.

        :param group_name: Group name
        :param user_login: User login
        :param organization: organization key.
        :return:
        """
        params = {
            'login': user_login,
            'name': group_name,
            'organization': organization
        }

        self.post(API_USER_GROUPS_REMOVE_USER_ENDPOINT, params=params)

    def search_users_belong_to_group(self, group_name, organization, q=None, selected="selected"):
        """
        Search for users with membership information with respect to a group.

        :param group_name: Group name
        :param organization: organization key.
        :param q: Limit search to names or logins that contain the supplied string.
        :param selected: Depending on the value, show only selected items (selected=selected), deselected items
          (selected=deselected), or all items with their selection status (selected=all).Possible values are for:
            * all
            * deselected
            * selected
          default value is selected.
        :return:
        """
        params = {
            'name': group_name,
            'organization': organization,
            'selected': selected
        }
        page_num = 1
        page_size = 1
        total = 2

        if q:
            params.update({'q': q})

        while page_num * page_size < total:
            resp = self.get(API_USER_GROUPS_USERS_ENDPOINT, params=params)
            response = resp.json()

            page_num = response['p']
            page_size = response['ps']
            total = response['total']

            params['p'] = page_num + 1

            for user in response['users']:
                yield user
