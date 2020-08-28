#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.config import (
    API_PROJECTS_BULK_DELETE_ENDPOINT,
    API_PROJECTS_SEARCH_ENDPOINT,
    API_PROJECTS_CREATE_ENDPOINT,
    API_PROJECTS_DELETE_ENDPOINT,
    API_PROJECTS_UPDATE_VISIBILITY_ENDPOINT,
    API_PROJECTS_UPDATE_KEY_ENDPOINT
)


class SonarQubeProject:
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube
        self._data = None

    def poll(self):
        self._data = self.search_projects()

    def iterkeys(self):
        """

        :return:
        """
        for item in self:
            yield item['key']

    def keys(self):
        """

        :return:
        """
        return list(self.iterkeys())

    def __len__(self):
        """

        :return:
        """
        return len(self.keys())

    def __contains__(self, project_key):
        """

        :param project_key:
        :return:
        """
        result = self.search_projects()
        project_keys = [item['key'] for item in result]
        return project_key in project_keys

    def __getitem__(self, index):
        """
        :param index:
        :return:
        """
        return list(self)[index]

    def __iter__(self):
        """

        :return:
        """
        self.poll()
        return self._data

    def search_projects(self, analyzedBefore=None, onProvisionedOnly="false", projects=None, q=None, qualifiers="TRK"):
        """
        Search for projects or views to administrate them.

        :param analyzedBefore: Filter the projects for which last analysis is older than the given date (exclusive).
          Either a date (server timezone) or datetime can be provided.
        :param onProvisionedOnly: Filter the projects that are provisioned. default value is false.
        :param projects: Comma-separated list of project keys
        :param q:
          Limit search to:
            * component names that contain the supplied string
            * component keys that contain the supplied string
        :param qualifiers: Comma-separated list of component qualifiers. Filter the results with the specified
          qualifiers. Possible values are for:
            * TRK
            * VW
            * APP
          default value is TRK.

        :return:
        """
        params = {
            'onProvisionedOnly': onProvisionedOnly,
            'qualifiers': qualifiers.upper()
        }
        page_num = 1
        page_size = 1
        total = 2

        if analyzedBefore:
            params.update({'analyzedBefore': analyzedBefore})

        if projects:
            params.update({'projects': projects})

        if q:
            params.update({'q': q})

        while page_num * page_size < total:
            resp = self.sonarqube.make_call('get', API_PROJECTS_SEARCH_ENDPOINT, **params)
            response = resp.json()

            page_num = response['paging']['pageIndex']
            page_size = response['paging']['pageSize']
            total = response['paging']['total']

            params['p'] = page_num + 1

            for component in response['components']:
                yield component

    def create_project(self, project, name, visibility=None):
        """
        Create a project.

        :param project: Key of the project
        :param name: Name of the project. If name is longer than 500, it is abbreviated.
        :param visibility: Whether the created project should be visible to everyone, or only specific user/groups.
          If no visibility is specified, the default project visibility of the organization will be used.
          Possible values are for:
            * private
            * public
        :return:
        """
        params = {
            'name': name,
            'project': project
        }
        if visibility:
            params.update({'visibility': visibility})

        self.sonarqube.make_call('post', API_PROJECTS_CREATE_ENDPOINT, **params)

    def get_project_id(self, project_key):
        """
        get project id

        :param project_key:
        :return:
        """
        components = self.sonarqube.components.get_project_component_and_ancestors(project_key)
        return components['component']['id']

    def delete_project(self, project):
        """
        Delete a project.

        :param project: Project key
        :return:
        """
        params = {
            'project': project
        }
        self.sonarqube.make_call('post', API_PROJECTS_DELETE_ENDPOINT, **params)

    def bulk_delete_projects(self, analyzedBefore=None, onProvisionedOnly="false", projects=None,
                             q=None, qualifiers="TRK"):
        """
        Delete one or several projects.
        At least one parameter is required among analyzedBefore, projects, projectIds (deprecated since 6.4) and q

        :param analyzedBefore: Filter the projects for which last analysis is older than the given date (exclusive).
          Either a date (server timezone) or datetime can be provided.
        :param onProvisionedOnly: Filter the projects that are provisioned.default value is false.
        :param projects: Comma-separated list of project keys
        :param q:
          Limit to:
            * component names that contain the supplied string
            * component keys that contain the supplied string
        :param qualifiers: Comma-separated list of component qualifiers. Filter the results with the specified
          qualifiers. Possible values are for:
            * TRK
            * VW
            * APP
          default value is TRK.
        :return:
        """
        params = {
            'onProvisionedOnly': onProvisionedOnly,
            'qualifiers': qualifiers.upper()
        }

        if analyzedBefore:
            params.update({'analyzedBefore': analyzedBefore})

        if projects:
            params.update({'projects': projects})

        if q:
            params.update({'q': q})

        self.sonarqube.make_call('post', API_PROJECTS_BULK_DELETE_ENDPOINT, **params)

    def update_project_key(self, previous_project_key, new_project_key):
        """
        Update a project or module key and all its sub-components keys.

        :param previous_project_key: Project or module key
        :param new_project_key: New component key
        :return:
        """
        params = {
            'from': previous_project_key,
            'to': new_project_key
        }
        self.sonarqube.make_call('post', API_PROJECTS_UPDATE_KEY_ENDPOINT, **params)

    def update_project_visibility(self, project, visibility):
        """
        Updates visibility of a project.

        :param project: Project key
        :param visibility: New visibility
        :return:
        """
        params = {
            'project': project,
            'visibility': visibility
        }
        self.sonarqube.make_call('post', API_PROJECTS_UPDATE_VISIBILITY_ENDPOINT, **params)
