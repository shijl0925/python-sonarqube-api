#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_USER_GROUPS_SEARCH_ENDPOINT,
    API_USER_GROUPS_CREATE_ENDPOINT,
    API_USER_GROUPS_DELETE_ENDPOINT,
    API_USER_GROUPS_UPDATE_ENDPOINT,
    API_USER_GROUPS_USERS_ENDPOINT,
    API_USER_GROUPS_ADD_USER_ENDPOINT,
    API_USER_GROUPS_REMOVE_USER_ENDPOINT
)
from sonarqube.utils.common import POST


class SonarQubeUserGroups(RestClient):
    """
    SonarQube user_groups Operations
    """
    special_attributes_map = {
        'group_name': 'name',
        'group_id': 'id',
        'user_login': 'login'
    }

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeUserGroups, self).__init__(**kwargs)

    def __getitem__(self, name):
        result = list(self.search_user_groups(q=name))
        for group in result:
            if group['name'] == name:
                return group

    def search_user_groups(self, fields=None, q=None):
        """
        Search for user groups.

        :param fields: Comma-separated list of the fields to be returned in response.
          All the fields are returned by default. Possible values are for:
            * name
            * description
            * membersCount
        :param q: Limit search to names that contain the supplied string.
        :return:
        """
        params = {}

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

    @POST(API_USER_GROUPS_CREATE_ENDPOINT)
    def create_group(self, group_name, description=None):
        """
        Create a group.

        :param group_name: Name for the new group. A group name cannot be larger than 255 characters and must be unique.
          The value 'anyone' (whatever the case) is reserved and cannot be used.
        :param description: Description for the new group. A group description cannot be larger than 200 characters.
        :return: request response
        """

    @POST(API_USER_GROUPS_DELETE_ENDPOINT)
    def delete_group(self, group_name):
        """
        Delete a group. The default groups cannot be deleted.

        :param group_name: group name
        :return:
        """

    @POST(API_USER_GROUPS_UPDATE_ENDPOINT)
    def update_group(self, group_id, group_name=None, description=None):
        """
        Update a group.

        :param group_id: Identifier of the group.
        :param group_name: New optional name for the group. A group name cannot be larger than 255 characters and must
          be unique. Value 'anyone' (whatever the case) is reserved and cannot be used. If value is empty or not
          defined, then name is not changed.
        :param description: New optional description for the group. A group description cannot be larger than
          200 characters. If value is not defined, then description is not changed.
        :return:
        """

    @POST(API_USER_GROUPS_ADD_USER_ENDPOINT)
    def add_user_to_group(self, group_name, user_login):
        """
        Add a user to a group.

        :param group_name: Group name
        :param user_login: User login
        :return:
        """

    @POST(API_USER_GROUPS_REMOVE_USER_ENDPOINT)
    def remove_user_from_group(self, group_name, user_login):
        """
        Remove a user from a group.

        :param group_name: Group name
        :param user_login: User login
        :return:
        """

    def search_users_belong_to_group(self, group_name, q=None, selected="selected"):
        """
        Search for users with membership information with respect to a group.

        :param group_name: Group name
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
