#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube import SonarQubeClient

if __name__ == "__main__":
    url = 'http://localhost:9000'
    username = "admin"
    password = "admin"
    sonar = SonarQubeClient(sonarqube_url=url, username=username, password=password)

    # Create a new project link.
    sonar.project_links.create_project_link(projectKey="my_project", name="Custom", url="http://example.com")

    # Delete existing project link.
    sonar.project_links.delete_project_link(link_id=17)

    # List links of a project.
    project_links = sonar.project_links.search_project_links(projectKey="my_project")
