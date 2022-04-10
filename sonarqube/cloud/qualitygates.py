#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.community.qualitygates import SonarQubeQualityGates
from sonarqube.utils.config import (
    API_QUALITYGATES_LIST_ENDPOINT,
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
)
from sonarqube.utils.common import GET, POST, PAGES_GET


class SonarCloudQualityGates(SonarQubeQualityGates):
    """
    SonarCloud quality gates Operations
    """

    @POST(API_QUALITYGATES_COPY_ENDPOINT)
    def copy_quality_gate(self, id, name, organization):
        """
        Copy a Quality Gate.

        :param id: The ID of the source quality gate
        :param name: The name of the quality gate to create
        :param organization: Organization key.
        :return:
        """

    @POST(API_QUALITYGATES_CREATE_ENDPOINT)
    def create_quality_gate(self, name, organization):
        """
        Create a Quality Gate.

        :param name: The name of the quality gate to create
        :param organization: Organization key.
        :return: request response
        """

    @POST(API_QUALITYGATES_DESTROY_ENDPOINT)
    def delete_quality_gate(self, id, organization):
        """
        Delete a Quality Gate.

        :param id: ID of the quality gate to delete
        :param organization: Organization key.
        :return:
        """

    @POST(API_QUALITYGATES_RENAME_ENDPOINT)
    def rename_quality_gate(self, id, name, organization):
        """
        Rename a Quality Gate.

        :param id: ID of the quality gate to rename
        :param name: New name of the quality gate
        :param organization: Organization key.
        :return:
        """

    @POST(API_QUALITYGATES_CREATE_CONDITION_ENDPOINT)
    def create_condition_to_quality_gate(
        self, gateId, organization, metric, error, op=None
    ):
        """
        Add a new condition to a quality gate.

        :param gateId: ID of the quality gate
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

    @POST(API_QUALITYGATES_DELETE_CONDITION_ENDPOINT)
    def delete_condition_from_quality_gate(self, id, organization):
        """
        Delete a condition from a quality gate.

        :param id: Condition ID
        :param organization: Organization key.
        :return:
        """

    @POST(API_QUALITYGATES_UPDATE_CONDITION_ENDPOINT)
    def update_condition_to_quality_gate(
        self, id, organization, metric, error, op=None
    ):
        """
        Update a condition attached to a quality gate.

        :param id: Condition ID
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

    @PAGES_GET(API_QUALITYGATES_SEARCH_ENDPOINT, item="results")
    def get_qualitygate_projects(
        self, gateId, organization, selected="selected", query=None
    ):
        """
        Search for projects associated (or not) to a quality gate.

        :param gateId: Quality Gate ID
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

    @POST(API_QUALITYGATES_SET_AS_DEFAULT_ENDPOINT)
    def set_default_qualitygate(self, id, organization):
        """
        Set a quality gate as the default quality gate.

        :param id: ID of the quality gate to set as default
        :param organization: Organization key.
        :return:
        """

    @GET(API_QUALITYGATES_LIST_ENDPOINT)
    def get_quality_gates(self, organization):
        """
        Get a list of quality gates

        :param organization: Organization key. If no organization is provided, the default organization is used.
        :return:
        """

    @POST(API_QUALITYGATES_SELECT_ENDPOINT)
    def select_quality_gate_for_project(self, projectKey, gateId, organization):
        """
        Associate a project to a quality gate.

        :param projectKey: Project key
        :param gateId: Quality gate id
        :param organization: Organization key.
        :return:
        """

    @POST(API_QUALITYGATES_DESELECT_ENDPOINT)
    def remove_project_from_quality_gate(self, projectKey, organization):
        """
        Remove the association of a project from a quality gate.

        :param projectKey: Project key
        :param organization: Organization key.
        :return:
        """

    @GET(API_QUALITYGATES_SHOW_ENDPOINT)
    def show_quality_gate(self, name, organization):
        """
        Display the details of a quality gate.

        :param name: Name of the quality gate.
        :param organization: Organization key.
        :return:
        """

    @GET(API_QUALITYGATES_GET_BY_PROJECT_ENDPOINT)
    def get_quality_gate_of_project(self, project, organization):
        """
        Get the quality gate of a project.

        :param project: Project key
        :param organization: Organization key.
        :return:
        """
