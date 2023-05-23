#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_NOTIFICATIONS_LIST_ENDPOINT,
    API_NOTIFICATIONS_ADD_ENDPOINT,
    API_NOTIFICATIONS_REMOVE_ENDPOINT,
)
from sonarqube.utils.common import GET, POST


class SonarQubeNotifications(RestClient):
    """
    SonarQube notifications Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeNotifications, self).__init__(**kwargs)

    @GET(API_NOTIFICATIONS_LIST_ENDPOINT)
    def get_user_notifications(self, login):
        """
        SINCE 6.3
        List notifications of the authenticated user.

        :param login: User login
        :return:
        """

    @POST(API_NOTIFICATIONS_ADD_ENDPOINT)
    def add_notification_for_user(
        self, login, type, channel="EmailNotificationChannel", project=None
    ):
        """
        SINCE 6.3
        Add a notification for the authenticated user.

        :param login: User login
        :param type: Notification type.
          Possible values are for:
            * Global notifications: CeReportTaskFailure, ChangesOnMyIssue, NewAlerts, SQ-MyNewIssues
            * Per project notifications: CeReportTaskFailure, ChangesOnMyIssue, NewAlerts, NewFalsePositiveIssue,
              NewIssues, SQ-MyNewIssues
        :param channel: Channel through which the notification is sent. For example, notifications can be sent by email.
          default value is EmailNotificationChannel.
        :param project: Project key
        :return:
        """

    @POST(API_NOTIFICATIONS_REMOVE_ENDPOINT)
    def remove_notification_for_user(
        self, login, type, channel="EmailNotificationChannel", project=None
    ):
        """
        SINCE 6.3
        Remove a notification for the authenticated user.

        :param login: User login
        :param type: Notification type.
          Possible values are for:
            * Global notifications: CeReportTaskFailure, ChangesOnMyIssue, NewAlerts, SQ-MyNewIssues
            * Per project notifications: CeReportTaskFailure, ChangesOnMyIssue, NewAlerts, NewFalsePositiveIssue,
              NewIssues, SQ-MyNewIssues
        :param channel: Channel through which the notification is sent. For example, notifications can be sent by email.
          default value is EmailNotificationChannel.
        :param project: Project key
        :return:
        """
