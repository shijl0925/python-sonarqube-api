#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.config import (
    API_PLUGINS_AVAILABLE_ENDPOINT,
    API_PLUGINS_CANCEL_ALL_ENDPOINT,
    API_PLUGINS_INSTALL_ENDPOINT,
    API_PLUGINS_INSTALLED_ENDPOINT,
    API_PLUGINS_PENDING_ENDPOINT,
    API_PLUGINS_UNINSTALL_ENDPOINT,
    API_PLUGINS_UPDATE_ENDPOINT,
    API_PLUGINS_UPDATES_ENDPOINT
)


class SonarQubePlugins:
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def get_available_plugins(self):
        """
        Get the list of all the plugins available for installation on the SonarQube instance, sorted by plugin name.
        Plugin information is retrieved from Update Center. Date and time at which Update Center was last refreshed is
        provided in the response. Update status values are:

          * COMPATIBLE: plugin is compatible with current SonarQube instance.
          * INCOMPATIBLE: plugin is not compatible with current SonarQube instance.
          * REQUIRES_SYSTEM_UPGRADE: plugin requires SonarQube to be upgraded before being installed.
          * DEPS_REQUIRE_SYSTEM_UPGRADE: at least one plugin on which the plugin is dependent requires SonarQube to be upgraded.

        :return:
        """
        resp = self.sonarqube.make_call('get', API_PLUGINS_AVAILABLE_ENDPOINT)
        response = resp.json()
        return response['plugins']

    def cancel_operation_pending_plugins(self):
        """
        Cancels any operation pending on any plugin (install, update or uninstall)

        :return:
        """
        self.sonarqube.make_call('post', API_PLUGINS_CANCEL_ALL_ENDPOINT)

    def install_plugin(self, plugin_key):
        """
        Installs the latest version of a plugin specified by its key.
        Plugin information is retrieved from Update Center.

        :param plugin_key: The key identifying the plugin to install
        :return:
        """
        params = {
            'key': plugin_key
        }

        self.sonarqube.make_call('post', API_PLUGINS_INSTALL_ENDPOINT, **params)

    def get_installed_plugins(self, fields=None):
        """
        Get the list of all the plugins installed on the SonarQube instance, sorted by plugin name.

        :param fields: Comma-separated list of the additional fields to be returned in response.
          No additional field is returned by default. Possible values are:
            * category - category as defined in the Update Center. A connection to the Update Center is needed
        :return:
        """
        params = {}
        if fields:
            params.update({'f': fields})

        resp = self.sonarqube.make_call('get', API_PLUGINS_INSTALLED_ENDPOINT, **params)
        response = resp.json()
        return response['plugins']

    def get_pending_plugins(self):
        """
        Get the list of plugins which will either be installed or removed at the next startup of the SonarQube instance,
        sorted by plugin name.

        :return:
        """
        resp = self.sonarqube.make_call('get', API_PLUGINS_PENDING_ENDPOINT)
        return resp.json()

    def uninstall_plugin(self, plugin_key):
        """
        Uninstalls the plugin specified by its key.

        :param plugin_key: The key identifying the plugin to uninstall
        :return:
        """
        params = {
            'key': plugin_key
        }

        self.sonarqube.make_call('post', API_PLUGINS_UNINSTALL_ENDPOINT, **params)

    def update_plugin(self, plugin_key):
        """
        Updates a plugin specified by its key to the latest version compatible with the SonarQube instance.
        Plugin information is retrieved from Update Center.

        :param plugin_key: The key identifying the plugin to update
        :return:
        """
        params = {
            'key': plugin_key
        }

        self.sonarqube.make_call('post', API_PLUGINS_UPDATE_ENDPOINT, **params)

    def get_available_update_plugins(self):
        """
        Lists plugins installed on the SonarQube instance for which at least one newer version is available,
        sorted by plugin name. Each newer version is listed, ordered from the oldest to the newest,
        with its own update/compatibility status.Plugin information is retrieved from Update Center.
        Date and time at which Update Center was last refreshed is provided in the response.
        Update status values are: [COMPATIBLE, INCOMPATIBLE, REQUIRES_UPGRADE, DEPS_REQUIRE_UPGRADE].

        :return:
        """
        resp = self.sonarqube.make_call('get', API_PLUGINS_UPDATES_ENDPOINT)
        return resp.json()
