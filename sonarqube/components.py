#!/usr/bin/env python
# -*- coding:utf-8 -*-
from .config import *


class SonarQubeComponents(object):
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def get_project_component(self, component):
        """
        :param component: Component key
        :return:
        """
        params = {
            'component': component
        }

        resp = self.sonarqube._make_call('get', RULES_COMPONTENTS_SHOW_ENDPOINT, **params)
        data = resp.json()
        return data['component']

    def get_components(self, qualifiers, **kwargs):
        """
        :param qualifiers:Comma-separated list of component qualifiers. Filter the results with the specified qualifiers. Possible values are:
                          BRC - Sub-projects
                          DIR - Directories
                          FIL - Files
                          TRK - Projects
                          UTS - Test Files
        :param kwargs:
        :return:
        """
        params = {'qualifiers': qualifiers}
        if kwargs:
            self.sonarqube.copy_dict(params, kwargs)

        page_num = 1
        page_size = 1
        total = 2

        while page_num * page_size < total:
            resp = self.sonarqube._make_call('get', RULES_COMPONTENTS_SEARCH_ENDPOINT, **params)
            response = resp.json()

            page_num = response['paging']['pageIndex']
            page_size = response['paging']['pageSize']
            total = response['paging']['total']

            params['p'] = page_num + 1

            for component in response['components']:
                yield component

    def get_components_tree(self, component, **kwargs):
        """
        :param component: Base component key. The search is based on this component.
        :param kwargs:
        qualifiers:Comma-separated list of component qualifiers. Filter the results with the specified qualifiers. Possible values are:
                          BRC - Sub-projects
                          DIR - Directories
                          FIL - Files
                          TRK - Projects
                          UTS - Test Files
        component: Base component key. The search is based on this component.
        :return:
        """
        params = {'component': component}
        if kwargs:
            self.sonarqube.copy_dict(params, kwargs)

        page_num = 1
        page_size = 1
        total = 2

        while page_num * page_size < total:
            resp = self.sonarqube._make_call('get', RULES_COMPONTENTS_TREE_ENDPOINT, **params)
            response = resp.json()

            page_num = response['paging']['pageIndex']
            page_size = response['paging']['pageSize']
            total = response['paging']['total']

            params['p'] = page_num + 1

            for component in response['components']:
                yield component