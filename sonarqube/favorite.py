#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.config import (
    API_FAVORITES_ADD_ENDPOINT,
    API_FAVORITES_REMOVE_ENDPOINT,
    API_FAVORITES_SEARCH_ENDPOINT
)


class SonarQubeFavorites:
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def get_favorites(self):
        """
        Search for the authenticated user favorites.
        :return:
        """
        params = {}
        page_num = 1
        page_size = 1
        total = 2

        while page_num * page_size < total:
            resp = self.sonarqube.make_call('get', API_FAVORITES_SEARCH_ENDPOINT, **params)
            response = resp.json()

            page_num = response['paging']['pageIndex']
            page_size = response['paging']['pageSize']
            total = response['paging']['total']

            params['p'] = page_num + 1

            for favorite in response['favorites']:
                yield favorite

    def add_favorites(self, component):
        """
        Add a component (project, file etc.) as favorite for the authenticated user.
        :param component: Component key. Only components with qualifiers TRK, VW, SVW, APP, FIL, UTS are supported
        :return:
        """
        params = {
            'component': component
        }
        self.sonarqube.make_call('post', API_FAVORITES_ADD_ENDPOINT, **params)

    def remove_favorites(self, component):
        """
        Remove a component (project, directory, file etc.) as favorite for the authenticated user.
        :param component: Component key
        :return:
        """
        params = {
            'component': component
        }
        self.sonarqube.make_call('post', API_FAVORITES_REMOVE_ENDPOINT, **params)
