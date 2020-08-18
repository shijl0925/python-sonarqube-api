# -*- coding:utf-8 -*-
from sonarqube.config import (
    API_QUALITYGATES_LIST_ENDPOINT,
    API_QUALITYGATES_PROJECT_STATUS_ENDPOINT,
    API_QUALITYGATES_SELECT_ENDPOINT,
    API_QUALITYGATES_DESELECT_ENDPOINT,
    API_QUALITYGATES_SHOW_ENDPOINT,
    API_QUALITYGATES_GET_BY_PROJECT_ENDPOINT
)


class SonarQubeQualityGates:
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def get_qualitygates_project_status(self, project_key, branch):
        """
        Get the quality gate status of a project or a Compute Engine task. return 'ok','WARN','ERROR'
        :param project_key:
        :param branch
        :return:
        """
        params = {
            'projectKey': project_key,
            'branch': branch
        }
        resp = self.sonarqube.make_call('get', API_QUALITYGATES_PROJECT_STATUS_ENDPOINT, **params)
        data = resp.json()
        return data['projectStatus']

    def get_quality_gates(self):
        """
        Get a list of quality gates
        :return:
        """
        resp = self.sonarqube.make_call('get', API_QUALITYGATES_LIST_ENDPOINT)
        data = resp.json()
        return data['qualitygates']

    def select_quality_gate_for_project(self, project_key, gate_id):
        """
        Associate a project to a quality gate.
        :param project_key:
        :param gate_id:
        :return:
        """
        params = {'gateId': gate_id, 'projectKey': project_key}
        self.sonarqube.make_call('post', API_QUALITYGATES_SELECT_ENDPOINT, **params)

    def remove_project_from_quality_gate(self, project_key):
        """
        Remove the association of a project from a quality gate.
        :param project_key:
        :return:
        """
        params = {'projectKey': project_key}
        self.sonarqube.make_call('post', API_QUALITYGATES_DESELECT_ENDPOINT, **params)

    def show_quality_gate(self, gateId=None, name=None):
        """
        Display the details of a quality gate.
        :param gateId:
        :param name:
        :return:
        """
        params = {}
        if gateId:
            params.update({'id': gateId})
        if name:
            params.update({'name': name})
        resp = self.sonarqube.make_call('get', API_QUALITYGATES_SHOW_ENDPOINT, **params)
        data = resp.json()
        return data

    def get_quality_gate_of_project(self, project_key):
        """
        Get the quality gate of a project.
        :param project_key:
        :return:
        """
        params = {'project': project_key}
        resp = self.sonarqube.make_call('get', API_QUALITYGATES_GET_BY_PROJECT_ENDPOINT, **params)
        data = resp.json()
        return data['qualityGate']
