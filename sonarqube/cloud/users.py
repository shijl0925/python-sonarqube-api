#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.community.users import SonarQubeBaseUsers
from sonarqube.utils.config import API_USERS_GROUPS_ENDPOINT
from sonarqube.utils.common import GET


class SonarCloudUsers(SonarQubeBaseUsers):
    """
    SonarCloud users Operations
    """

    @GET(API_USERS_GROUPS_ENDPOINT)
    def search_groups_user_belongs_to(
        self, login, organization, q=None, selected="selected", p=None, ps=None
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
        :param p: page number.
        :param ps: Page size. Must be greater than 0 and less or equal than 500
        :return:
        """
