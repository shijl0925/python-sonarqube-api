#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube import SonarQubeClient

if __name__ == "__main__":
    url = 'http://localhost:9000'
    username = "admin"
    password = "admin"
    sonar = SonarQubeClient(sonarqube_url=url, username=username, password=password)

    # List the branches of a project.
    branches = sonar.project_branches.search_project_branches(project="my-project")

    # Delete a non-main branch of a project.
    sonar.project_branches.delete_project_branch(project="my_project", branch="branch1")

    # Rename the main branch of a project
    sonar.project_branches.rename_project_branch(project="my_project", name="branch1")
