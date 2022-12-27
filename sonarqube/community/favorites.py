#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_FAVORITES_ADD_ENDPOINT,
    API_FAVORITES_REMOVE_ENDPOINT,
    API_FAVORITES_SEARCH_ENDPOINT,
)
from sonarqube.utils.common import GET, POST


class SonarQubeFavorites(RestClient):
    """
    SonarQube favorites Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeFavorites, self).__init__(**kwargs)

    @GET(API_FAVORITES_SEARCH_ENDPOINT)
    def search_favorites(self, p=None, ps=None):
        """
        SINCE 6.3
        Search for the authenticated user favorites.
        :param p: page number.
        :param ps: Page size. Must be greater than 0 and less or equal than 500

        :return:
        """

    @POST(API_FAVORITES_ADD_ENDPOINT)
    def add_component_to_favorites(self, component):
        """
        SINCE 6.3
        Add a component (project, file etc.) as favorite for the authenticated user.

        :param component: Component key. Only components with qualifiers TRK, VW, SVW, APP, FIL, UTS are supported
        :return:
        """

    @POST(API_FAVORITES_REMOVE_ENDPOINT)
    def remove_component_from_favorites(self, component):
        """
        SINCE 6.3
        Remove a component (project, directory, file etc.) as favorite for the authenticated user.

        :param component: Component key
        :return:
        """
