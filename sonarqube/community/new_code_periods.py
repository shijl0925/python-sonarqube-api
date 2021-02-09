#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_NEW_CODE_PERIODS_LIST_ENDPOINT,
    API_NEW_CODE_PERIODS_SET_ENDPOINT,
    API_NEW_CODE_PERIODS_SHOW_ENDPOINT,
    API_NEW_CODE_PERIODS_UNSET_ENDPOINT,
)
from sonarqube.utils.common import GET, POST


class SonarQubeNewcodeperiods(RestClient):
    """
    SonarQube new code periods Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeNewcodeperiods, self).__init__(**kwargs)

    @GET(API_NEW_CODE_PERIODS_LIST_ENDPOINT)
    def list(self, project):
        """
        SINCE 8.0
        List the New Code Periods for all branches in a project.

        :param project: Project key
        :return:
        """

    @POST(API_NEW_CODE_PERIODS_SET_ENDPOINT)
    def set(self, type, project=None, branch=None, value=None):
        """
        SINCE 8.0
        Updates the setting for the New Code Period on different levels:
          * Project key must be provided to update the value for a project
          * Both project and branch keys must be provided to update the value for a branch

        :param type: Type
          New code periods of the following types are allowed:
          * SPECIFIC_ANALYSIS - can be set at branch level only
          * PREVIOUS_VERSION - can be set at any level (global, project, branch)
          * NUMBER_OF_DAYS - can be set at any level (global, project, branch)
          * REFERENCE_BRANCH - can only be set for projects and branches
        :param project: Project key
        :param branch: Branch key
        :param value: Value
          For each type, a different value is expected:
          * the uuid of an analysis, when type is SPECIFIC_ANALYSIS
          * no value, when type is PREVIOUS_VERSION
          * a number, when type is NUMBER_OF_DAYS
          * a string, when type is REFERENCE_BRANCH
        :return:
        """

    @GET(API_NEW_CODE_PERIODS_SHOW_ENDPOINT)
    def show(self, project=None, branch=None):
        """
        SINCE 8.0
        Shows a setting for the New Code Period.

        :param project: Project key
        :param branch: Branch key
        :return:
        """

    @POST(API_NEW_CODE_PERIODS_UNSET_ENDPOINT)
    def unset(self, project=None, branch=None):
        """
        SINCE 8.0
        Unset the New Code Period setting for a branch, project or global.

        :param project: Project key
        :param branch: Branch key
        :return:
        """