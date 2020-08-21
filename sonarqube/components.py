#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.config import (
    API_COMPONTENTS_SHOW_ENDPOINT,
    API_COMPONTENTS_SEARCH_ENDPOINT,
    API_COMPONTENTS_TREE_ENDPOINT
)


class SonarQubeComponents:
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def get_project_component(self, component):
        """
        Returns a component (file, directory, project, view…) and its ancestors. The ancestors are ordered from the
        parent to the root project. The 'componentId' or 'component' parameter must be provided.
        :param component: Component key
        :return:
        """
        params = {
            'component': component
        }

        resp = self.sonarqube.make_call('get', API_COMPONTENTS_SHOW_ENDPOINT, **params)
        return resp.json()

    def get_components(self, qualifiers, **kwargs):
        """
        Search for components
        :param qualifiers:Comma-separated list of component qualifiers. Filter the results with
        the specified qualifiers. Possible values are:
        * BRC - Sub-projects
        * DIR - Directories
        * FIL - Files
        * TRK - Projects
        * UTS - Test Files
        :param kwargs:
        language: Language key. If provided, only components for the given language are returned.
        p: 1-based page number, default value is 1
        ps: Page size. Must be greater than 0 and less or equal than 500, default value is 100
        q: Limit search to:
          * component names that contain the supplied string
          * component keys that are exactly the same as the supplied string
        :return:
        """
        params = {'qualifiers': qualifiers}
        if kwargs:
            self.sonarqube.copy_dict(params, kwargs)

        page_num = 1
        page_size = 1
        total = 2

        while page_num * page_size < total:
            resp = self.sonarqube.make_call('get', API_COMPONTENTS_SEARCH_ENDPOINT, **params)
            response = resp.json()

            page_num = response['paging']['pageIndex']
            page_size = response['paging']['pageSize']
            total = response['paging']['total']

            params['p'] = page_num + 1

            for component in response['components']:
                yield component

    def get_components_tree(self, component, **kwargs):
        """
        Navigate through components based on the chosen strategy.
        :param component: Base component key. The search is based on this component.
        :param kwargs:
        asc: Ascending sort
        p: 1-based page number, default value is 1
        ps: Page size. Must be greater than 0 and less or equal than 500, default value is 100
        q: Limit search to:
          * component names that contain the supplied string
          * component keys that are exactly the same as the supplied string
        qualifiers:Comma-separated list of component qualifiers. Filter the results with
          the specified qualifiers. Possible values are:
        * BRC - Sub-projects
        * DIR - Directories
        * FIL - Files
        * TRK - Projects
        * UTS - Test Files
        s: Comma-separated list of sort fields,such as: name, path, qualifier, and default value is name
        strategy: Strategy to search for base component descendants:
          * children: return the children components of the base component. Grandchildren components are not returned
          * all: return all the descendants components of the base component. Grandchildren are returned.
          * leaves: return all the descendant components (files, in general) which don't have other children.
            They are the leaves of the component tree.
        :return:
        """
        params = {'component': component}
        if kwargs:
            self.sonarqube.copy_dict(params, kwargs)

        page_num = 1
        page_size = 1
        total = 2

        while page_num * page_size < total:
            resp = self.sonarqube.make_call('get', API_COMPONTENTS_TREE_ENDPOINT, **params)
            response = resp.json()

            page_num = response['paging']['pageIndex']
            page_size = response['paging']['pageSize']
            total = response['paging']['total']

            params['p'] = page_num + 1

            for item in response['components']:
                yield item
