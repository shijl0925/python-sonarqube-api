#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_USER_GROUPS_SEARCH_ENDPOINT,
    API_USER_GROUPS_CREATE_ENDPOINT,
    API_USER_GROUPS_UPDATE_ENDPOINT,
)
from sonarqube.utils.common import GET, POST


class SonarQubeUserGroups(RestClient):
    """
    SonarQube user_groups Operations
    """

    def get_user_group(self, name, organization=None):
        result = self.search_user_groups(organization=organization, q=name)
        groups = result.get("groups", [])
        item = None
        for group in groups:
            if group["name"] == name:
                item = group
                break

        return item

    @GET(API_USER_GROUPS_SEARCH_ENDPOINT)
    def search_user_groups(self, organization=None, f=None, managed=None, q=None, p=None, ps=None):
        """
        SINCE 5.2
        Search for user groups.

        :param organization: organization key.
        :param f: Comma-separated list of the fields to be returned in response.
          All the fields are returned by default. Possible values are for:
            * name
            * description
            * membersCount
        :param managed: Return managed or non-managed groups.
          Only available for managed instances, throws for non-managed instances. (since 10.0)
        :param p: page number.
        :param ps: Page size. Must be greater than 0 and less or equal than 500
        :param q: Limit search to names that contain the supplied string.
        :return:
        """

    @POST(API_USER_GROUPS_CREATE_ENDPOINT)
    def create_group(self, name, organization=None, description=None):
        """
        SINCE 5.2
        Create a group.

        :param name: Name for the new group. A group name cannot be larger than 255 characters and must be unique.
          The value 'anyone' (whatever the case) is reserved and cannot be used.
        :param organization: organization key.
        :param description: Description for the new group. A group description cannot be larger than 200 characters.
        :return: request response
        """
    @POST(API_USER_GROUPS_UPDATE_ENDPOINT)
    def update_group(self, currentName, name=None, description=None):
        """
        SINCE 5.2
        Update a group.

        :param currentName: Name of the group to be updated. (since 8.5)
        :param name: New optional name for the group. A group name cannot be larger than 255 characters and must
          be unique. Value 'anyone' (whatever the case) is reserved and cannot be used. If value is empty or not
          defined, then name is not changed.
        :param description: New optional description for the group. A group description cannot be larger than
          200 characters. If value is not defined, then description is not changed.
        :return:
        """
