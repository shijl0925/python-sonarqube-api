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
    API_USER_GROUPS_REMOVE_USER_ENDPOINT,
)
from sonarqube.utils.common import POST, PAGES_GET


class SonarQubeUserGroups(RestClient):
    """
    SonarQube user_groups Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeUserGroups, self).__init__(**kwargs)

    def get(self, name):
        result = list(self.search_user_groups(q=name))
        for group in result:
            if group["name"] == name:
                return group

    @PAGES_GET(API_USER_GROUPS_SEARCH_ENDPOINT, item="groups")
    def search_user_groups(self, f=None, q=None):
        """
        SINCE 5.2
        Search for user groups.

        :param f: Comma-separated list of the fields to be returned in response.
          All the fields are returned by default. Possible values are for:
            * name
            * description
            * membersCount
        :param q: Limit search to names that contain the supplied string.
        :return:
        """

    @POST(API_USER_GROUPS_CREATE_ENDPOINT)
    def create_group(self, name, description=None):
        """
        SINCE 5.2
        Create a group.

        :param name: Name for the new group. A group name cannot be larger than 255 characters and must be unique.
          The value 'anyone' (whatever the case) is reserved and cannot be used.
        :param description: Description for the new group. A group description cannot be larger than 200 characters.
        :return: request response
        """

    @POST(API_USER_GROUPS_DELETE_ENDPOINT)
    def delete_group(self, name):
        """
        SINCE 5.2
        Delete a group. The default groups cannot be deleted.

        :param name: group name
        :return:
        """

    @POST(API_USER_GROUPS_UPDATE_ENDPOINT)
    def update_group(self, id, name=None, description=None):
        """
        SINCE 5.2
        Update a group.

        :param id: Identifier of the group.
        :param name: New optional name for the group. A group name cannot be larger than 255 characters and must
          be unique. Value 'anyone' (whatever the case) is reserved and cannot be used. If value is empty or not
          defined, then name is not changed.
        :param description: New optional description for the group. A group description cannot be larger than
          200 characters. If value is not defined, then description is not changed.
        :return:
        """

    @POST(API_USER_GROUPS_ADD_USER_ENDPOINT)
    def add_user_to_group(self, name, login):
        """
        SINCE 5.2
        Add a user to a group.

        :param name: Group name
        :param login: User login
        :return:
        """

    @POST(API_USER_GROUPS_REMOVE_USER_ENDPOINT)
    def remove_user_from_group(self, name, login):
        """
        SINCE 5.2
        Remove a user from a group.

        :param name: Group name
        :param login: User login
        :return:
        """

    @PAGES_GET(API_USER_GROUPS_USERS_ENDPOINT, item="users")
    def search_users_belong_to_group(self, name, q=None, selected="selected"):
        """
        SINCE 5.2
        Search for users with membership information with respect to a group.

        :param name: Group name
        :param q: Limit search to names or logins that contain the supplied string.
        :param selected: Depending on the value, show only selected items (selected=selected), deselected items
          (selected=deselected), or all items with their selection status (selected=all).Possible values are for:
            * all
            * deselected
            * selected
          default value is selected.
        :return:
        """
