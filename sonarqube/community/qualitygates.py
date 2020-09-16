#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
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


class SonarQubeQualityGates(RestClient):
    """
    SonarQube quality gates Operations
    """
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeQualityGates, self).__init__(**kwargs)

    def copy_quality_gate(self, source_id, gate_name, organization=None):
        """
        Copy a Quality Gate.

        :param source_id: The ID of the source quality gate
        :param gate_name: The name of the quality gate to create
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """
        params = {'id': source_id, 'name': gate_name}

        if organization:
            params.update({"organization": organization})

        self.post(API_QUALITYGATES_COPY_ENDPOINT, params=params)

    def create_quality_gate(self, gate_name, organization=None):
        """
        Create a Quality Gate.

        :param gate_name: The name of the quality gate to create
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return: request response
        """
        params = {'name': gate_name}
        if organization:
            params.update({"organization": organization})

        return self.post(API_QUALITYGATES_CREATE_ENDPOINT, params=params)

    def delete_quality_gate(self, gate_id, organization=None):
        """
        Delete a Quality Gate.

        :param gate_id: ID of the quality gate to delete
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """
        params = {'id': gate_id}
        if organization:
            params.update({"organization": organization})

        self.post(API_QUALITYGATES_DESTROY_ENDPOINT, params=params)

    def rename_quality_gate(self, gate_id, gate_name, organization=None):
        """
        Rename a Quality Gate.

        :param gate_id: ID of the quality gate to rename
        :param gate_name: New name of the quality gate
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """
        params = {'id': gate_id, 'name': gate_name}
        if organization:
            params.update({"organization": organization})

        self.post(API_QUALITYGATES_RENAME_ENDPOINT, params=params)

    def create_condition_to_quality_gate(self, gate_id, metric, error, op=None, organization=None):
        """
        Add a new condition to a quality gate.

        :param gate_id: ID of the quality gate
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
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return: request response
        """
        params = {
            'gateId': gate_id,
            'metric': metric.upper(),
            'error': error
        }

        if op:
            params.update({'op': op.upper()})

        if organization:
            params.update({"organization": organization})

        return self.post(API_QUALITYGATES_CREATE_CONDITION_ENDPOINT, params=params)

    def delete_condition_from_quality_gate(self, condition_id, organization=None):
        """
        Delete a condition from a quality gate.

        :param condition_id: Condition ID
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """
        params = {'id': condition_id}
        if organization:
            params.update({"organization": organization})

        self.post(API_QUALITYGATES_DELETE_CONDITION_ENDPOINT, params=params)

    def update_condition_to_quality_gate(self, condition_id, metric, error, op=None, organization=None):
        """
        Update a condition attached to a quality gate.

        :param condition_id: Condition ID
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
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """
        params = {
            'id': condition_id,
            'metric': metric.upper(),
            'error': error
        }

        if op:
            params.update({'op': op.upper()})

        if organization:
            params.update({"organization": organization})

        self.post(API_QUALITYGATES_UPDATE_CONDITION_ENDPOINT, params=params)

    def get_qualitygate_projects(self, gate_id, selected="selected", query=None, organization=None):
        """
        Search for projects associated (or not) to a quality gate.

        :param gate_id: Quality Gate ID
        :param selected: Depending on the value, show only selected items (selected=selected),
          deselected items (selected=deselected), or all items with their selection status (selected=all).
          Possible values are for:
            * all
            * deselected
            * selected
          default value is selected
        :param query: To search for projects containing this string.
          If this parameter is set, "selected" is set to "all".
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """
        params = {
            'gateId': gate_id,
            'selected': selected
        }
        if query:
            params.update({"query": query})

        if organization:
            params.update({"organization": organization})

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

    def set_default_qualitygate(self, gate_id, organization=None):
        """
        Set a quality gate as the default quality gate.

        :param gate_id: ID of the quality gate to set as default
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """
        params = {'id': gate_id}
        if organization:
            params.update({"organization": organization})

        self.post(API_QUALITYGATES_SET_AS_DEFAULT_ENDPOINT, params=params)

    def get_project_qualitygates_status(self, project_key=None, analysis_id=None, branch=None, pull_request_id=None):
        """
        Get the quality gate status of a project or a Compute Engine task. return 'ok','WARN','ERROR'
        The NONE status is returned when there is no quality gate associated with the analysis.
        Returns an HTTP code 404 if the analysis associated with the task is not found or does not exist.

        :param project_key: Project key
        :param analysis_id: Analysis id
        :param branch: Branch key
        :param pull_request_id:
        :return:
        """
        params = {}
        if project_key:
            params.update({'projectKey': project_key})

            if branch:
                params.update({'branch': branch})

            if pull_request_id:
                params.update({'pullRequest': pull_request_id})

        elif analysis_id:
            params.update({'analysisId': analysis_id})

        resp = self.get(API_QUALITYGATES_PROJECT_STATUS_ENDPOINT, params=params)
        response = resp.json()
        return response['projectStatus']

    def get_quality_gates(self, organization=None):
        """
        Get a list of quality gates

        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """
        params = {}
        if organization:
            params.update({"organization": organization})

        resp = self.get(API_QUALITYGATES_LIST_ENDPOINT, params=params)
        response = resp.json()
        return response['qualitygates']

    def select_quality_gate_for_project(self, project_key, gate_id, organization=None):
        """
        Associate a project to a quality gate.

        :param project_key: Project key
        :param gate_id: Quality gate id
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """
        params = {'gateId': gate_id, 'projectKey': project_key}
        if organization:
            params.update({"organization": organization})

        self.post(API_QUALITYGATES_SELECT_ENDPOINT, params=params)

    def remove_project_from_quality_gate(self, project_key, organization=None):
        """
        Remove the association of a project from a quality gate.

        :param project_key: Project key
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """
        params = {'projectKey': project_key}
        if organization:
            params.update({"organization": organization})

        self.post(API_QUALITYGATES_DESELECT_ENDPOINT, params=params)

    def show_quality_gate(self, gate_name, organization=None):
        """
        Display the details of a quality gate.

        :param gate_name: Name of the quality gate.
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """
        params = {'name': gate_name}

        if organization:
            params.update({"organization": organization})

        resp = self.get(API_QUALITYGATES_SHOW_ENDPOINT, params=params)
        response = resp.json()
        return response

    def get_quality_gate_of_project(self, project_key, organization=None):
        """
        Get the quality gate of a project.

        :param project_key: Project key
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """
        params = {'project': project_key}
        if organization:
            params.update({"organization": organization})

        resp = self.get(API_QUALITYGATES_GET_BY_PROJECT_ENDPOINT, params=params)
        response = resp.json()
        return response['qualityGate']
