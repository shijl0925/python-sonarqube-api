#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.config import (
    API_SETTINGS_SET_ENDPOINT,
    API_SETTINGS_RESET_ENDPOINT,
    API_SETTINGS_VALUES_ENDPOINT,
    API_SETTINGS_LIST_DEFINITIONS_ENDPOINT
)


class SonarQubeSettings:
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def update_setting_value(self, setting_key, setting_value, component_key=None, fieldValues=None):
        """
        Update a setting value.
        The settings defined in conf/sonar.properties are read-only and can't be changed.
        :param setting_key: Setting key
        :param setting_value: Setting value. To reset a value, please use the reset web service.
        :param component_key: Component key
        :param fieldValues: Setting field values. To set several values, the parameter must be called once for
          each value.
        :return:
        """
        params = {
            'key': setting_key,
            'value': setting_value
        }
        if component_key:
            params.update({"component": component_key})

        if fieldValues:
            params.update({"fieldValues": fieldValues})

        self.sonarqube.make_call('post', API_SETTINGS_SET_ENDPOINT, **params)

    def remove_setting_value(self, setting_keys, component_key=None):
        """
        Remove a setting value.
        The settings defined in conf/sonar.properties are read-only and can't be changed.
        :param setting_keys: Comma-separated list of keys
        :param component_key: Component key
        :return:
        """
        params = {
            'keys': setting_keys
        }
        if component_key:
            params.update({"component": component_key})

        self.sonarqube.make_call('post', API_SETTINGS_RESET_ENDPOINT, **params)

    def get_settings_values(self, component_key=None, setting_keys=None):
        """
        List settings values.
        If no value has been set for a setting, then the default value is returned.
        The settings from conf/sonar.properties are excluded from results.
        :param component_key: Component key
        :param setting_keys: List of setting keys
        :return:
        """
        params = {}
        if component_key:
            params.update({"component": component_key})

        if setting_keys:
            params.update({"keys": setting_keys})

        resp = self.sonarqube.make_call('get', API_SETTINGS_VALUES_ENDPOINT, **params)
        response = resp.json()
        return response['settings']

    def get_settings_definitions(self, component_key=None):
        """
        List settings definitions.
        :param component_key: Component key
        :return:
        """
        params = {}
        if component_key:
            params.update({"component": component_key})

        resp = self.sonarqube.make_call('get', API_SETTINGS_LIST_DEFINITIONS_ENDPOINT, **params)
        response = resp.json()
        return response['definitions']
