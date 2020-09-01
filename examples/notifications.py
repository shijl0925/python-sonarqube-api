#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube import SonarQubeClient

if __name__ == "__main__":
    url = 'http://localhost:9000'
    username = "admin"
    password = "admin"
    sonar = SonarQubeClient(sonarqube_url=url, username=username, password=password)

    # List notifications of the authenticated user.
    user_notifications = sonar.notifications.get_user_notifications(login="kevin")

    # Add a notification for the authenticated user.
    sonar.notifications.add_notification_for_user(login="kevin", notification_type="CeReportTaskFailure")
    # or
    sonar.notifications.add_notification_for_user(login="kevin", notification_type="ChangesOnMyIssue", project="my_project")

    # Remove a notification for the authenticated user.
    sonar.notifications.remove_notification_for_user(login="kevin", notification_type="CeReportTaskFailure")
    # or
    sonar.notifications.remove_notification_for_user(login="kevin", notification_type="ChangesOnMyIssue", project="my_project")
