#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube import SonarQubeClient

if __name__ == "__main__":
    url = 'http://localhost:9000'
    username = "admin"
    password = "admin"
    sonar = SonarQubeClient(sonarqube_url=url, username=username, password=password)

    # Search tags
    project_tags = sonar.project_tags.search_project_tags()

    # Set tags on a project.
    sonar.project_tags.set_project_tags(project="my_project", tags="finance,offshore")
