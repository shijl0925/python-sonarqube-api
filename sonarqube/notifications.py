#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.config import (
    API_NOTIFICATIONS_LIST_ENDPOINT,
    API_NOTIFICATIONS_ADD_ENDPOINT,
    API_NOTIFICATIONS_REMOVE_ENDPOINT
)


class SonarQubeNotification:
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def user_list_notifications(self, login):
        """
        List notifications of the authenticated user.
        :param login: User login
        :return:
        """
        params = {
            'login': login
        }
        resp = self.sonarqube.make_call('get', API_NOTIFICATIONS_LIST_ENDPOINT, **params)
        data = resp.json()
        return data['notifications']

    def user_add_notifications(self, login, notification_type, **kwargs):
        """
        Add a notification for the authenticated user.
        :param login: User login
        :param notification_type: Notification type. Possible values are for:
          * Global notifications: CeReportTaskFailure, ChangesOnMyIssue, NewAlerts, SQ-MyNewIssues
          * Per project notifications: CeReportTaskFailure, ChangesOnMyIssue, NewAlerts, NewFalsePositiveIssue,
            NewIssues, SQ-MyNewIssues
        :param kwargs:
        channel: Channel through which the notification is sent. For example, notifications can be sent by email.
        project: Project key
        :return:
        """
        params = {
            'login': login,
            'type': notification_type
        }
        if kwargs:
            self.sonarqube.copy_dict(params, kwargs)

        self.sonarqube.make_call('post', API_NOTIFICATIONS_ADD_ENDPOINT, **params)

    def user_remove_notifications(self, login, notification_type, **kwargs):
        """
        Remove a notification for the authenticated user.
        :param login: User login
        :param notification_type: Notification type. Possible values are for:
          * Global notifications: CeReportTaskFailure, ChangesOnMyIssue, NewAlerts, SQ-MyNewIssues
          * Per project notifications: CeReportTaskFailure, ChangesOnMyIssue, NewAlerts, NewFalsePositiveIssue,
            NewIssues, SQ-MyNewIssues
        :param kwargs:
        channel: Channel through which the notification is sent. For example, notifications can be sent by email.
        project: Project key
        :return:
        """
        params = {
            'login': login,
            'type': notification_type
        }
        if kwargs:
            self.sonarqube.copy_dict(params, kwargs)

        self.sonarqube.make_call('post', API_NOTIFICATIONS_REMOVE_ENDPOINT, **params)
