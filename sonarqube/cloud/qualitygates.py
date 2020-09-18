#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.community.qualitygates import SonarQubeQualityGates
from sonarqube.utils.config import (
    API_QUALITYGATES_LIST_ENDPOINT,
    API_QUALITYGATES_PROJECT_STATUS_ENDPOINT,
    API_QUALITYGATES_SELECT_ENDPOINT,
    API_QUALITYGATES_DESELECT_ENDPOINT,
    API_QUALITYGATES_SHOW_ENDPOINT,
    API_QUALITYGATES_GET_BY_PROJECT_ENDPOINT,
    API_QUALITYGATES_COPY_ENDPOINT,
    API_QUALITYGATES_CREATE_ENDPOINT,
    API_QUALITYGATES_DESTROY_ENDPOINT,
    API_QUALITYGATES_RENAME_ENDPOINT,
    API_QUALITYGATES_CREATE_CONDITION_ENDPOINT,
    API_QUALITYGATES_DELETE_CONDITION_ENDPOINT,
    API_QUALITYGATES_UPDATE_CONDITION_ENDPOINT,
    API_QUALITYGATES_SEARCH_ENDPOINT,
    API_QUALITYGATES_SET_AS_DEFAULT_ENDPOINT
)


class SonarCloudQualityGates(SonarQubeQualityGates):
    """
    SonarCloud quality gates Operations
    """

    def copy_quality_gate(self, source_id, gate_name, organization):
        """
        Copy a Quality Gate.

        :param source_id: The ID of the source quality gate
        :param gate_name: The name of the quality gate to create
        :param organization: Organization key.
        :return:
        """
        params = {
            'id': source_id,
            'name': gate_name,
            'organization': organization
        }

        self.post(API_QUALITYGATES_COPY_ENDPOINT, params=params)

    def create_quality_gate(self, gate_name, organization):
        """
        Create a Quality Gate.

        :param gate_name: The name of the quality gate to create
        :param organization: Organization key.
        :return: request response
        """
        params = {
            'name': gate_name,
            'organization': organization
        }

        return self.post(API_QUALITYGATES_CREATE_ENDPOINT, params=params)

    def delete_quality_gate(self, gate_id, organization):
        """
        Delete a Quality Gate.

        :param gate_id: ID of the quality gate to delete
        :param organization: Organization key.
        :return:
        """
        params = {'id': gate_id}
        if organization:
            params.update({"organization": organization})

        self.post(API_QUALITYGATES_DESTROY_ENDPOINT, params=params)

    def rename_quality_gate(self, gate_id, gate_name, organization):
        """
        Rename a Quality Gate.

        :param gate_id: ID of the quality gate to rename
        :param gate_name: New name of the quality gate
        :param organization: Organization key.
        :return:
        """
        params = {
            'id': gate_id,
            'name': gate_name,
            'organization': organization
        }

        self.post(API_QUALITYGATES_RENAME_ENDPOINT, params=params)

    def create_condition_to_quality_gate(self, gate_id, organization, metric, error, op=None):
        """
        Add a new condition to a quality gate.

        :param gate_id: ID of the quality gate
        :param organization: Organization key.
        :param metric: Condition metric.
          Only metric of the following types are allowed:
            * INT
            * MILLISEC
            * RATING
            * WORK_DUR
            * FLOAT
            * PERCENT
            * LEVEL
        :param error: Condition error threshold
        :param op: Condition operator
          Possible values are for:
            * LT = is lower than
            * GT = is greater than

        :return: request response
        """
        params = {
            'gateId': gate_id,
            'metric': metric.upper(),
            'organization': organization,
            'error': error
        }

        if op:
            params.update({'op': op.upper()})

        return self.post(API_QUALITYGATES_CREATE_CONDITION_ENDPOINT, params=params)

    def delete_condition_from_quality_gate(self, condition_id, organization):
        """
        Delete a condition from a quality gate.

        :param condition_id: Condition ID
        :param organization: Organization key.
        :return:
        """
        params = {
            'id': condition_id,
            'organization': organization
        }

        self.post(API_QUALITYGATES_DELETE_CONDITION_ENDPOINT, params=params)

    def update_condition_to_quality_gate(self, condition_id, organization, metric, error, op=None):
        """
        Update a condition attached to a quality gate.

        :param condition_id: Condition ID
        :param organization: Organization key.
        :param metric: Condition metric.
          Only metric of the following types are allowed:
            * INT
            * MILLISEC
            * RATING
            * WORK_DUR
            * FLOAT
            * PERCENT
            * LEVEL
        :param error: Condition error threshold
        :param op: Condition operator
          Possible values are for:
            * LT = is lower than
            * GT = is greater than

        :return:
        """
        params = {
            'id': condition_id,
            'organization': organization,
            'metric': metric.upper(),
            'error': error
        }

        if op:
            params.update({'op': op.upper()})

        self.post(API_QUALITYGATES_UPDATE_CONDITION_ENDPOINT, params=params)

    def get_qualitygate_projects(self, gate_id, organization, selected="selected", query=None):
        """
        Search for projects associated (or not) to a quality gate.

        :param gate_id: Quality Gate ID
        :param organization: Organization key.
        :param selected: Depending on the value, show only selected items (selected=selected),
          deselected items (selected=deselected), or all items with their selection status (selected=all).
          Possible values are for:
            * all
            * deselected
            * selected
          default value is selected
        :param query: To search for projects containing this string.
          If this parameter is set, "selected" is set to "all".

        :return:
        """
        params = {
            'gateId': gate_id,
            'organization': organization,
            'selected': selected
        }
        if query:
            params.update({"query": query})

        page_num = 1
        page_size = 1
        total = 2

        while page_num * page_size < total:
            resp = self.get(API_QUALITYGATES_SEARCH_ENDPOINT, params=params)
            response = resp.json()

            page_num = response['paging']['pageIndex']
            page_size = response['paging']['pageSize']
            total = response['paging']['total']

            params['p'] = page_num + 1

            for result in response['results']:
                yield result

    def set_default_qualitygate(self, gate_id, organization):
        """
        Set a quality gate as the default quality gate.

        :param gate_id: ID of the quality gate to set as default
        :param organization: Organization key.
        :return:
        """
        params = {
            'id': gate_id,
            'organization': organization
        }

        self.post(API_QUALITYGATES_SET_AS_DEFAULT_ENDPOINT, params=params)

    def get_quality_gates(self, organization):
        """
        Get a list of quality gates

        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """
        params = {"organization": organization}

        resp = self.get(API_QUALITYGATES_LIST_ENDPOINT, params=params)
        response = resp.json()
        return response['qualitygates']

    def select_quality_gate_for_project(self, project_key, gate_id, organization):
        """
        Associate a project to a quality gate.

        :param project_key: Project key
        :param gate_id: Quality gate id
        :param organization: Organization key.
        :return:
        """
        params = {
            'gateId': gate_id,
            'projectKey': project_key,
            'organization': organization
        }

        self.post(API_QUALITYGATES_SELECT_ENDPOINT, params=params)

    def remove_project_from_quality_gate(self, project_key, organization):
        """
        Remove the association of a project from a quality gate.

        :param project_key: Project key
        :param organization: Organization key.
        :return:
        """
        params = {
            'projectKey': project_key,
            'organization': organization
        }

        self.post(API_QUALITYGATES_DESELECT_ENDPOINT, params=params)

    def show_quality_gate(self, gate_name, organization):
        """
        Display the details of a quality gate.

        :param gate_name: Name of the quality gate.
        :param organization: Organization key.
        :return:
        """
        params = {
            'name': gate_name,
            'organization': organization
        }

        resp = self.get(API_QUALITYGATES_SHOW_ENDPOINT, params=params)
        response = resp.json()
        return response

    def get_quality_gate_of_project(self, project_key, organization):
        """
        Get the quality gate of a project.

        :param project_key: Project key
        :param organization: Organization key.
        :return:
        """
        params = {
            'project': project_key,
            'organization': organization
        }

        resp = self.get(API_QUALITYGATES_GET_BY_PROJECT_ENDPOINT, params=params)
        response = resp.json()
        return response['qualityGate']
