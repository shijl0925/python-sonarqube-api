#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube import SonarQubeClient

if __name__ == "__main__":
    url = 'http://localhost:9000'
    username = "admin"
    password = "admin"
    sonar = SonarQubeClient(sonarqube_url=url, username=username, password=password)

    """ authenticate a user """
    sonar.auth.authenticate_user(login="kevin", password="xxx")

    """ logout a user. """
    sonar.auth.logout_user()

    """ check credentials """
    print(sonar.auth.check_credentials())
