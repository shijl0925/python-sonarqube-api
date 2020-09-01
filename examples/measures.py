#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube import SonarQubeClient

if __name__ == "__main__":
    url = 'http://localhost:9000'
    username = "admin"
    password = "admin"
    sonar = SonarQubeClient(sonarqube_url=url, username=username, password=password)

    """ Return component with specified measures """
    component = sonar.measures.get_component_with_specified_measures(component="my_project",
                                                                     branch="develop",
                                                                     additionalFields="metrics,periods",
                                                                     metricKeys="code_smells,bugs,vulnerabilities")

    """
    Navigate through components based on the chosen strategy with specified measures. The baseComponentId or
    the component parameter must be provided.
    """
    component_tree = sonar.measures.get_component_tree_with_specified_measures(component_key="my_project",
                                                                               branch="develop",
                                                                               metricKeys="code_smells,bugs,vulnerabilities")

    """ Search measures history of a component """
    measures_history = sonar.measures.search_measures_history(component="my_project", branch="develop")
