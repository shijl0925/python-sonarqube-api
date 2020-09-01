#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube import SonarQubeClient

if __name__ == "__main__":
    url = 'http://localhost:9000'
    username = "admin"
    password = "admin"
    sonar = SonarQubeClient(sonarqube_url=url, username=username, password=password)

    """ Search for the authenticated user favorites """
    favorites = sonar.favorites.search_favorites()

    """ Add a component (project, file etc.) as favorite for the authenticated user """
    sonar.favorites.add_component_to_favorites(component="my_project")
    # or
    sonar.favorites.add_component_to_favorites(component="my_project:/src/foo/Bar.php")

    """ Remove a component (project, directory, file etc.) as favorite for the authenticated user """
    sonar.favorites.remove_component_from_favorites(component="my_project")
    # or
    sonar.favorites.remove_component_from_favorites(component="my_project:/src/foo/Bar.php")
