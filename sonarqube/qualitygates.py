#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.config import (
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


class SonarQubeQualityGates:
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def copy_quality_gate(self, source_id, gate_name):
        """
        Copy a Quality Gate.

        :param source_id: The ID of the source quality gate
        :param gate_name: The name of the quality gate to create
        :return:
        """
        params = {'id': source_id, 'name': gate_name}
        self.sonarqube.make_call('post', API_QUALITYGATES_COPY_ENDPOINT, **params)

    def create_quality_gate(self, gate_name):
        """
        Create a Quality Gate.

        :param gate_name: The name of the quality gate to create
        :return: Returns id and name of quality gate
        """
        params = {'name': gate_name}
        res = self.sonarqube.make_call('post', API_QUALITYGATES_CREATE_ENDPOINT, **params)
        return res

    def delete_quality_gate(self, gate_id):
        """
        Delete a Quality Gate.

        :param gate_id: ID of the quality gate to delete
        :return:
        """
        params = {'id': gate_id}
        self.sonarqube.make_call('post', API_QUALITYGATES_DESTROY_ENDPOINT, **params)

    def rename_quality_gate(self, gate_id, gate_name):
        """
        Rename a Quality Gate.

        :param gate_id: ID of the quality gate to rename
        :param gate_name: New name of the quality gate
        :return:
        """
        params = {'id': gate_id, 'name': gate_name}
        self.sonarqube.make_call('post', API_QUALITYGATES_RENAME_ENDPOINT, **params)

    def create_condition_to_quality_gate(self, gate_id, metric, error, op=None):
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
        :return:
        """
        params = {
            'gateId': gate_id,
            'metric': metric.upper(),
            'error': error
        }
        if op:
            params.update({'op': op.upper()})

        self.sonarqube.make_call('post', API_QUALITYGATES_CREATE_CONDITION_ENDPOINT, **params)

    def delete_condition_from_quality_gate(self, condition_id):
        """
        Delete a condition from a quality gate.

        :param condition_id: Condition ID
        :return:
        """
        params = {'id': condition_id}
        self.sonarqube.make_call('post', API_QUALITYGATES_DELETE_CONDITION_ENDPOINT, **params)

    def update_condition_to_quality_gate(self, condition_id, metric, error, op=None):
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
        :return:
        """
        params = {
            'id': condition_id,
            'metric': metric.upper(),
            'error': error
        }
        if op:
            params.update({'op': op.upper()})

        self.sonarqube.make_call('post', API_QUALITYGATES_UPDATE_CONDITION_ENDPOINT, **params)

    def get_qualitygate_projects(self, gate_id, selected="selected"):
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
        :return:
        """
        params = {
            'gateId': gate_id,
            'selected': selected
        }

        page_num = 1
        page_size = 1
        total = 2

        while page_num * page_size < total:
            resp = self.sonarqube.make_call('get', API_QUALITYGATES_SEARCH_ENDPOINT, **params)
            response = resp.json()

            page_num = response['paging']['pageIndex']
            page_size = response['paging']['pageSize']
            total = response['paging']['total']

            params['p'] = page_num + 1

            for result in response['results']:
                yield result

    def set_default_qualitygate(self, gate_id):
        """
        Set a quality gate as the default quality gate.

        :param gate_id: ID of the quality gate to set as default
        :return:
        """
        params = {'id': gate_id}
        self.sonarqube.make_call('post', API_QUALITYGATES_SET_AS_DEFAULT_ENDPOINT, **params)

    def get_project_qualitygates_status(self, project_key=None, analysis_id=None, branch=None):
        """
        Get the quality gate status of a project or a Compute Engine task. return 'ok','WARN','ERROR'
        The NONE status is returned when there is no quality gate associated with the analysis.
        Returns an HTTP code 404 if the analysis associated with the task is not found or does not exist.

        :param project_key: Project key
        :param analysis_id: Analysis id
        :param branch: Branch key
        :return:
        """
        params = {}
        if project_key:
            params.update({'projectKey': project_key})
            if branch:
                params.update({'branch': branch})
        elif analysis_id:
            params.update({'analysisId': analysis_id})

        resp = self.sonarqube.make_call('get', API_QUALITYGATES_PROJECT_STATUS_ENDPOINT, **params)
        response = resp.json()
        return response['projectStatus']

    def get_quality_gates(self):
        """
        Get a list of quality gates

        :return:
        """
        resp = self.sonarqube.make_call('get', API_QUALITYGATES_LIST_ENDPOINT)
        response = resp.json()
        return response['qualitygates']

    def select_quality_gate_for_project(self, project_key, gate_id):
        """
        Associate a project to a quality gate.

        :param project_key: Project key
        :param gate_id: Quality gate id
        :return:
        """
        params = {'gateId': gate_id, 'projectKey': project_key}
        self.sonarqube.make_call('post', API_QUALITYGATES_SELECT_ENDPOINT, **params)

    def remove_project_from_quality_gate(self, project_key):
        """
        Remove the association of a project from a quality gate.

        :param project_key: Project key
        :return:
        """
        params = {'projectKey': project_key}
        self.sonarqube.make_call('post', API_QUALITYGATES_DESELECT_ENDPOINT, **params)

    def show_quality_gate(self, gate_id=None, gate_name=None):
        """
        Display the details of a quality gate.

        :param gate_id: ID of the quality gate. Either id or name must be set
        :param gate_name: Name of the quality gate. Either id or name must be set
        :return:
        """
        params = {}
        if gate_id:
            params.update({'id': gate_id})
        elif gate_name:
            params.update({'name': gate_name})

        resp = self.sonarqube.make_call('get', API_QUALITYGATES_SHOW_ENDPOINT, **params)
        response = resp.json()
        return response

    def get_quality_gate_of_project(self, project_key):
        """
        Get the quality gate of a project.

        :param project_key: Project key
        :return:
        """
        params = {'project': project_key}
        resp = self.sonarqube.make_call('get', API_QUALITYGATES_GET_BY_PROJECT_ENDPOINT, **params)
        response = resp.json()
        return response['qualityGate']
