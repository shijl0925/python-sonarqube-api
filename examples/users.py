#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube import SonarQubeClient

if __name__ == "__main__":
    url = 'http://localhost:9000'
    username = "admin"
    password = "admin"
    sonar = SonarQubeClient(sonarqube_url=url, username=username, password=password)

    # Get a list of active users.
    users = sonar.users.search_users()

    # Create a user.
    sonar.users.create_user(login="sonar", name="SonarQube", password="sonar@123")

    # Update a user.
    sonar.users.update_user(login="sonar", email="sonar@wz-inc.com")

    # Deactivate a user.
    sonar.users.deactivate_user(login="new_sonar")

    # Update a user login. A login can be updated many times.
    sonar.users.update_user_login('sonar', 'new_sonar')
