#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .config import *

class SonarQubeNotification(object):
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def user_list_notifications(self, login):
        """
        获取用户提醒权限
        :param login:
        :return:
        """
        params = {
            'login': login
        }
        resp = self.sonarqube._make_call('get', RULES_NOTIFICATIONS_LIST_ENDPOINT, **params)
        data = resp.json()
        list_notifications = []
        for i in data['notifications']:
            list_notifications.append(i['type'])
        return list_notifications

    def user_add_notifications(self, login, type, project = None):
        """
        给用户添加提醒权限
        :param login:
        :param type:
        :param project:
        :return:
        """
        params = {
            'login': login,
            'type': type
        }
        if project:
            params['project'] = project

        self.sonarqube._make_call('post', RULES_NOTIFICATIONS_ADD_ENDPOINT, **params)

    def user_remove_notifications(self, login, type, project = None):
        """
        删除用户提醒权限
        :param login:
        :param type:
        :param project:
        :return:
        """
        params = {
            'login': login,
            'type': type
        }
        if project:
            params['project'] = project

        self.sonarqube._make_call('post', RULES_NOTIFICATIONS_REMOVE_ENDPOINT, **params)
