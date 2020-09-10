#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.rest_client import RestClient
from sonarqube.config import (
    API_FAVORITES_ADD_ENDPOINT,
    API_FAVORITES_REMOVE_ENDPOINT,
    API_FAVORITES_SEARCH_ENDPOINT
)


class SonarQubeFavorites(RestClient):
    """
    SonarQube favorites Operations
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeFavorites, self).__init__(**kwargs)

    def search_favorites(self):
        """
        Search for the authenticated user favorites.

        :return:
        """
        params = {}
        page_num = 1
        page_size = 1
        total = 2

        while page_num * page_size < total:
            resp = self.get(API_FAVORITES_SEARCH_ENDPOINT, params=params)
            response = resp.json()

            page_num = response['paging']['pageIndex']
            page_size = response['paging']['pageSize']
            total = response['paging']['total']

            params['p'] = page_num + 1

            for favorite in response['favorites']:
                yield favorite

    def add_component_to_favorites(self, component):
        """
        Add a component (project, file etc.) as favorite for the authenticated user.

        :param component: Component key. Only components with qualifiers TRK, VW, SVW, APP, FIL, UTS are supported
        :return:
        """
        params = {
            'component': component
        }

        self.post(API_FAVORITES_ADD_ENDPOINT, params=params)

    def remove_component_from_favorites(self, component):
        """
        Remove a component (project, directory, file etc.) as favorite for the authenticated user.

        :param component: Component key
        :return:
        """
        params = {
            'component': component
        }

        self.post(API_FAVORITES_REMOVE_ENDPOINT, params=params)
