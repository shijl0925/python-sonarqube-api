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
    API_QUALITYGATES_SET_AS_DEFAULT_ENDPOINT,
    API_QUALITYGATES_ADD_GROUP_ENDPOINT,
)
from sonarqube.utils.common import GET, POST, PAGES_GET


class SonarQubeQualityGates(RestClient):
    """
    SonarQube quality gates Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeQualityGates, self).__init__(**kwargs)

    @POST(API_QUALITYGATES_ADD_GROUP_ENDPOINT)
    def add_group_to_gate(self, gateName, groupName):
        """
        SINCE 9.2
        Allow a group of users to edit a Quality Gate.

        :param gateName: The name of the quality gate
        :param groupName: The name of the group that can administer the gate
        :return:
        """

    @POST(API_QUALITYGATES_COPY_ENDPOINT)
    def copy_quality_gate(self, id, name, organization=None):
        """
        SINCE 4.3
        Copy a Quality Gate.

        :param id: The ID of the source quality gate
        :param name: The name of the quality gate to create
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """

    @POST(API_QUALITYGATES_CREATE_ENDPOINT)
    def create_quality_gate(self, name, organization=None):
        """
        SINCE 4.3
        Create a Quality Gate.

        :param name: The name of the quality gate to create
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return: request response
        """

    @POST(API_QUALITYGATES_DESTROY_ENDPOINT)
    def delete_quality_gate(self, id, organization=None):
        """
        SINCE 4.3
        Delete a Quality Gate.

        :param id: ID of the quality gate to delete
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """

    @POST(API_QUALITYGATES_RENAME_ENDPOINT)
    def rename_quality_gate(self, id, name, organization=None):
        """
        SINCE 4.3
        Rename a Quality Gate.

        :param id: ID of the quality gate to rename
        :param name: New name of the quality gate
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """

    @POST(API_QUALITYGATES_CREATE_CONDITION_ENDPOINT)
    def create_condition_to_quality_gate(
        self, gateId, metric, error, op=None, organization=None
    ):
        """
        SINCE 4.3
        Add a new condition to a quality gate.

        :param gateId: ID of the quality gate
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

    @POST(API_QUALITYGATES_DELETE_CONDITION_ENDPOINT)
    def delete_condition_from_quality_gate(self, id, organization=None):
        """
        SINCE 4.3
        Delete a condition from a quality gate.

        :param id: Condition ID
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """

    @POST(API_QUALITYGATES_UPDATE_CONDITION_ENDPOINT)
    def update_condition_to_quality_gate(
        self, id, metric, error, op=None, organization=None
    ):
        """
        SINCE 4.3
        Update a condition attached to a quality gate.

        :param id: Condition ID
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

    @PAGES_GET(API_QUALITYGATES_SEARCH_ENDPOINT, item="results")
    def get_qualitygate_projects(
        self, gateId, selected="selected", query=None, organization=None
    ):
        """
        SINCE 4.3
        Search for projects associated (or not) to a quality gate.

        :param gateId: Quality Gate ID
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

    @POST(API_QUALITYGATES_SET_AS_DEFAULT_ENDPOINT)
    def set_default_qualitygate(self, id, organization=None):
        """
        SINCE 4.3
        Set a quality gate as the default quality gate.

        :param id: ID of the quality gate to set as default
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """

    @GET(API_QUALITYGATES_PROJECT_STATUS_ENDPOINT)
    def get_project_qualitygates_status(
        self, projectKey=None, analysisId=None, branch=None, pullRequest=None
    ):
        """
        SINCE 5.3
        Get the quality gate status of a project or a Compute Engine task. return 'ok','WARN','ERROR'
        The NONE status is returned when there is no quality gate associated with the analysis.
        Returns an HTTP code 404 if the analysis associated with the task is not found or does not exist.

        :param projectKey: Project key
        :param analysisId: Analysis id
        :param branch: Branch key
        :param pullRequest:
        :return:
        """

    @GET(API_QUALITYGATES_LIST_ENDPOINT)
    def get_quality_gates(self, organization=None):
        """
        SINCE 4.3
        Get a list of quality gates

        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """

    @POST(API_QUALITYGATES_SELECT_ENDPOINT)
    def select_quality_gate_for_project(self, projectKey, gateId, organization=None):
        """
        SINCE 4.3
        Associate a project to a quality gate.

        :param projectKey: Project key
        :param gateId: Quality gate id
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """

    @POST(API_QUALITYGATES_DESELECT_ENDPOINT)
    def remove_project_from_quality_gate(self, projectKey, organization=None):
        """
        SINCE 4.3
        Remove the association of a project from a quality gate.

        :param projectKey: Project key
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """

    @GET(API_QUALITYGATES_SHOW_ENDPOINT)
    def show_quality_gate(self, name, organization=None):
        """
        SINCE 4.3
        Display the details of a quality gate.

        :param name: Name of the quality gate.
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """

    @GET(API_QUALITYGATES_GET_BY_PROJECT_ENDPOINT)
    def get_quality_gate_of_project(self, project, organization=None):
        """
        SINCE 6.1
        Get the quality gate of a project.

        :param project: Project key
        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """
