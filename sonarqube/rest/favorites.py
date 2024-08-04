#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_FAVORITES_SEARCH_ENDPOINT,
)
from sonarqube.utils.common import GET


class SonarQubeFavorites(RestClient):
    """
    SonarQube favorites Operations
    """

    @GET(API_FAVORITES_SEARCH_ENDPOINT)
    def search_favorites(self, p=None, ps=None):
        """
        SINCE 6.3
        Search for the authenticated user favorites.
        :param p: page number.
        :param ps: Page size. Must be greater than 0 and less or equal than 500

        :return:
        """
