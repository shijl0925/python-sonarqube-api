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
    API_USER_GROUPS_REMOVE_USER_ENDPOINT,
)
from sonarqube.utils.common import GET, POST


class SonarCloudUserGroups(SonarQubeUserGroups):
    """
    SonarCloud user_groups Operations
    """

    def get(self, key):
        raise AttributeError(
            "%s does not support this method" % self.__class__.__name__
        )

    @GET(API_USER_GROUPS_SEARCH_ENDPOINT)
    def search_user_groups(self, organization, f=None, q=None, p=None, ps=None):
        """
        Search for user groups.

        :param organization: organization key.
        :param f: Comma-separated list of the fields to be returned in response.
          All the fields are returned by default. Possible values are for:
            * name
            * description
            * membersCount
        :param p: page number.
        :param ps: Page size. Must be greater than 0 and less or equal than 500
        :param q: Limit search to names that contain the supplied string.
        :return:
        """

    @POST(API_USER_GROUPS_CREATE_ENDPOINT)
    def create_group(self, name, organization, description=None):
        """
        Create a group.

        :param name: Name for the new group. A group name cannot be larger than 255 characters and must be unique.
          The value 'anyone' (whatever the case) is reserved and cannot be used.
        :param organization: organization key.
        :param description: Description for the new group. A group description cannot be larger than 200 characters.
        :return: request response
        """

    @POST(API_USER_GROUPS_DELETE_ENDPOINT)
    def delete_group(self, name, organization):
        """
        Delete a group. The default groups cannot be deleted.

        :param name: group name
        :param organization: organization key.
        :return:
        """

    @POST(API_USER_GROUPS_ADD_USER_ENDPOINT)
    def add_user_to_group(self, name, login, organization):
        """
        Add a user to a group.

        :param name: Group name
        :param login: User login
        :param organization: organization key.
        :return:
        """

    @POST(API_USER_GROUPS_REMOVE_USER_ENDPOINT)
    def remove_user_from_group(self, name, login, organization):
        """
        Remove a user from a group.

        :param name: Group name
        :param login: User login
        :param organization: organization key.
        :return:
        """

    @GET(API_USER_GROUPS_USERS_ENDPOINT)
    def search_users_belong_to_group(
        self, name, organization, q=None, selected="selected", p=None, ps=None
    ):
        """
        Search for users with membership information with respect to a group.

        :param name: Group name
        :param organization: organization key.
        :param q: Limit search to names or logins that contain the supplied string.
        :param selected: Depending on the value, show only selected items (selected=selected), deselected items
          (selected=deselected), or all items with their selection status (selected=all).Possible values are for:
            * all
            * deselected
            * selected
          default value is selected.
        :param p: page number.
        :param ps: Page size. Must be greater than 0 and less or equal than 500
        :return:
        """
