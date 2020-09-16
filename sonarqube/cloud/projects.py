#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_PROJECTS_BULK_DELETE_ENDPOINT,
    API_PROJECTS_SEARCH_ENDPOINT,
    API_PROJECTS_CREATE_ENDPOINT,
    API_PROJECTS_DELETE_ENDPOINT,
    API_PROJECTS_UPDATE_VISIBILITY_ENDPOINT,
    API_PROJECTS_UPDATE_KEY_ENDPOINT
)


class SonarCloudProjects(RestClient):
    """
    SonarCloud projects Operations
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarCloudProjects, self).__init__(**kwargs)

    def search_projects(self, organization, analyzedBefore=None, onProvisionedOnly=False, projects=None, q=None):
        """
        Search for projects or views to administrate them.

        :param organization: The key of the organization
        :param analyzedBefore: Filter the projects for which last analysis is older than the given date (exclusive).
          Either a date (server timezone) or datetime can be provided.
        :param onProvisionedOnly: Filter the projects that are provisioned.
          Possible values are for: True or False. default value is False.
        :param projects: Comma-separated list of project keys
        :param q:
          Limit search to:
            * component names that contain the supplied string
            * component keys that contain the supplied string

        :return:
        """
        params = {
            'onProvisionedOnly': onProvisionedOnly and 'true' or 'false',
            'organization': organization
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
            resp = self.get(API_PROJECTS_SEARCH_ENDPOINT, params=params)
            response = resp.json()

            page_num = response['paging']['pageIndex']
            page_size = response['paging']['pageSize']
            total = response['paging']['total']

            params['p'] = page_num + 1

            for component in response['components']:
                yield component

    def create_project(self, project, name, organization, visibility=None):
        """
        Create a project.

        :param project: Key of the project
        :param name: Name of the project. If name is longer than 500, it is abbreviated.
        :param organization: The key of the organization
        :param visibility: Whether the created project should be visible to everyone, or only specific user/groups.
          If no visibility is specified, the default project visibility of the organization will be used.
          Possible values are for:
            * private
            * public
        :return: request response
        """
        params = {
            'name': name,
            'project': project,
            'organization': organization
        }
        if visibility:
            params.update({'visibility': visibility})

        return self.post(API_PROJECTS_CREATE_ENDPOINT, params=params)

    def delete_project(self, project):
        """
        Delete a project.

        :param project: Project key
        :return:
        """
        params = {
            'project': project
        }

        self.post(API_PROJECTS_DELETE_ENDPOINT, params=params)

    def bulk_delete_projects(self, organization, analyzedBefore=None, onProvisionedOnly=False, projects=None,
                             q=None):
        """
        Delete one or several projects.
        At least one parameter is required among analyzedBefore, projects, projectIds (deprecated since 6.4) and q

        :param organization: The key of the organization
        :param analyzedBefore: Filter the projects for which last analysis is older than the given date (exclusive).
          Either a date (server timezone) or datetime can be provided.
        :param onProvisionedOnly: Filter the projects that are provisioned.
          Possible values are for: True or False. default value is False.
        :param projects: Comma-separated list of project keys
        :param q:
          Limit to:
            * component names that contain the supplied string
            * component keys that contain the supplied string

        :return:
        """
        params = {
            'onProvisionedOnly': onProvisionedOnly and 'true' or 'false',
            'organization': organization
        }

        if analyzedBefore:
            params.update({'analyzedBefore': analyzedBefore})

        if projects:
            params.update({'projects': projects})

        if q:
            params.update({'q': q})

        self.post(API_PROJECTS_BULK_DELETE_ENDPOINT, params=params)

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

        self.post(API_PROJECTS_UPDATE_KEY_ENDPOINT, params=params)

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

        self.post(API_PROJECTS_UPDATE_VISIBILITY_ENDPOINT, params=params)
