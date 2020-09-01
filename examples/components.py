#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube import SonarQubeClient

if __name__ == "__main__":
    url = 'http://localhost:9000'
    username = "admin"
    password = "admin"
    sonar = SonarQubeClient(sonarqube_url=url, username=username, password=password)

    """
    Returns a component (file, directory, project, view…) and its ancestors. The ancestors are ordered from the
    parent to the root project.
    """
    component = sonar.components.get_project_component_and_ancestors("BMW_SDK_CPP")

    """ Search for components """
    components = sonar.components.search_components(qualifiers="TRK", language="java")

    """
    Navigate through components based on the chosen strategy.
    When limiting search with the q parameter, directories are not returned.
    """
    components_tree = sonar.components.get_components_tree(component="my_project", qualifiers="TRK")
