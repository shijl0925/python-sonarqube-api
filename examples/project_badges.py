#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube import SonarQubeClient

if __name__ == "__main__":
    url = 'http://localhost:9000'
    username = "admin"
    password = "admin"
    sonar = SonarQubeClient(sonarqube_url=url, username=username, password=password)

    # Generate badge for project's measure as an SVG.
    project_measures_badge = sonar.project_badges.generate_badge_for_project_measures("my_project",
                                                                                      metric='code_smells')
    with open("project_measures_badge.html", 'w') as f:
        f.write(project_measures_badge)

    # Generate badge for project's quality gate as an SVG.
    quality_gate_badge = sonar.project_badges.generate_badge_for_project_quality_gate("my_project")
    with open("quality_gate_badge.html", 'w') as f:
        f.write(quality_gate_badge)
