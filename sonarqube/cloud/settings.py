#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_SETTINGS_SET_ENDPOINT,
    API_SETTINGS_RESET_ENDPOINT,
    API_SETTINGS_VALUES_ENDPOINT,
    API_SETTINGS_LIST_DEFINITIONS_ENDPOINT,
)
from sonarqube.utils.common import GET, POST


class SonarCloudSettings(RestClient):
    """
    SonarCloud settings Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarCloudSettings, self).__init__(**kwargs)

    @POST(API_SETTINGS_SET_ENDPOINT)
    def update_setting_value(
        self,
        key,
        value,
        component=None,
        branch=None,
        pullRequest=None,
        fieldValues=None,
    ):
        """
        Update a setting value.
        The settings defined in conf/sonar.properties are read-only and can't be changed.

        :param key: Setting key
        :param value: Setting value. To reset a value, please use the reset web service.
        :param component: Component key
        :param branch: Branch key. Only available on following settings : sonar.leak.period
        :param pullRequest: Pull request id. Only available on following settings : sonar.leak.period
        :param fieldValues: Setting field values. To set several values, the parameter must be called once for
          each value.
        :return:
        """

    @POST(API_SETTINGS_RESET_ENDPOINT)
    def remove_setting_value(self, keys, component=None, branch=None, pullRequest=None):
        """
        Remove a setting value.
        The settings defined in conf/sonar.properties are read-only and can't be changed.

        :param keys: Comma-separated list of keys
        :param component: Component key
        :param branch: Branch key
        :param pullRequest: Pull request id

        :return:
        """

    @GET(API_SETTINGS_VALUES_ENDPOINT)
    def get_settings_values(
        self, component=None, branch=None, pullRequest=None, keys=None
    ):
        """
        List settings values.
        If no value has been set for a setting, then the default value is returned.
        The settings from conf/sonar.properties are excluded from results.

        :param component: Component key
        :param branch: Branch key. Only available on following settings : sonar.leak.period
        :param pullRequest: Pull request id. Only available on following settings : sonar.leak.period
        :param keys: List of setting keys
        :return:
        """

    @GET(API_SETTINGS_LIST_DEFINITIONS_ENDPOINT)
    def get_settings_definitions(self, component=None, branch=None, pullRequest=None):
        """
        List settings definitions.

        :param component: Component key
        :param branch: Branch key. Only available on following settings : sonar.leak.period
        :param pullRequest: Pull request id. Only available on following settings : sonar.leak.period

        :return:
        """
