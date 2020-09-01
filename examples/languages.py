#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube import SonarQubeClient

if __name__ == "__main__":
    url = 'http://localhost:9000'
    username = "admin"
    password = "admin"
    sonar = SonarQubeClient(sonarqube_url=url, username=username, password=password)

    """ List supported programming languages """
    supported_programming_languages = sonar.languages.get_supported_programming_languages()
