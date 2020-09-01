#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube import SonarQubeClient

if __name__ == "__main__":
    url = 'http://localhost:9000'
    username = "admin"
    password = "admin"
    sonar = SonarQubeClient(sonarqube_url=url, username=username, password=password)

    # List the pull requests of a project.
    project_pull_requests = sonar.project_pull_requests.search_project_pull_requests(project="my_project")

    # Delete a pull request.
    sonar.project_pull_requests.delete_project_pull_requests(project="my_project", pullRequest=1543)
