#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.community.components import SonarQubeComponents
from sonarqube.utils.config import API_COMPONTENTS_SEARCH_ENDPOINT


class SonarCloudComponents(SonarQubeComponents):
    """
    SonarCloud components Operations
    """
    def search_components(self, organization, qualifiers, language=None, q=None):
        """
        Search for components

        :param organization: Organization key
        :param qualifiers: Comma-separated list of component qualifiers. Filter the results with
          the specified qualifiers. Possible values are:

          * BRC - Sub-projects
          * DIR - Directories
          * FIL - Files
          * TRK - Projects
          * UTS - Test Files

        :param language: Language key. If provided, only components for the given language are returned.
        :param q: Limit search to:

          * component names that contain the supplied string
          * component keys that are exactly the same as the supplied string

        :return:
        """
        params = {'organization': organization, 'qualifiers': qualifiers}
        if language:
            params.update({'language': language})

        if q:
            params.update({'q': q})

        page_num = 1
        page_size = 1
        total = 2

        while page_num * page_size < total:
            resp = self.get(API_COMPONTENTS_SEARCH_ENDPOINT, params=params)
            response = resp.json()

            page_num = response['paging']['pageIndex']
            page_size = response['paging']['pageSize']
            total = response['paging']['total']

            params['p'] = page_num + 1

            for component in response['components']:
                yield component
