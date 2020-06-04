#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .config import *


class SonarQubeNotification(object):
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def user_list_notifications(self, login):
        """
        List notifications of the authenticated user.
        :param login:
        :return:
        """
        params = {
            'login': login
        }
        resp = self.sonarqube._make_call('get', API_NOTIFICATIONS_LIST_ENDPOINT, **params)
        data = resp.json()
        return data['notifications']

    def user_add_notifications(self, login, type, **kwargs):
        """
        Add a notification for the authenticated user.
        :param login:
        :param type:
        :return:
        """
        params = {
            'login': login,
            'type': type
        }
        if kwargs:
            self.sonarqube.copy_dict(params, kwargs)

        self.sonarqube._make_call('post', API_NOTIFICATIONS_ADD_ENDPOINT, **params)

    def user_remove_notifications(self, login, type, **kwargs):
        """
        Remove a notification for the authenticated user.
        :param login:
        :param type:
        :return:
        """
        params = {
            'login': login,
            'type': type
        }
        if kwargs:
            self.sonarqube.copy_dict(params, kwargs)

        self.sonarqube._make_call('post', API_NOTIFICATIONS_REMOVE_ENDPOINT, **params)
