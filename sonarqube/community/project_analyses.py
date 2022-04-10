#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_PROJECT_ANALYSES_CREATE_EVENT_ENDPOINT,
    API_PROJECT_ANALYSES_DELETE_ENDPOINT,
    API_PROJECT_ANALYSES_DELETE_EVENT_ENDPOINT,
    API_PROJECT_ANALYSES_SEARCH_ENDPOINT,
    API_PROJECT_ANALYSES_SET_BASELINE_ENDPOINT,
    API_PROJECT_ANALYSES_UNSET_BASELINE_ENDPOINT,
    API_PROJECT_ANALYSES_UPDATE_EVENT_ENDPOINT,
)
from sonarqube.utils.common import POST, PAGES_GET


class SonarQubeProjectAnalyses(RestClient):
    """
    SonarQube project analyses Operations
    """

    special_attributes_map = {"from_date": "from", "to_date": "to"}

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeProjectAnalyses, self).__init__(**kwargs)

    @POST(API_PROJECT_ANALYSES_CREATE_EVENT_ENDPOINT)
    def create_project_analysis_event(self, analysis, name, category="OTHER"):
        """
        SINCE 6.3
        Create a project analysis event.Only event of category 'VERSION' and 'OTHER' can be created.

        :param analysis: Analysis key
        :param name: Name
        :param category: Category.
          Possible values are for:
            * VERSION
            * OTHER
          default value is OTHER.
        :return: request response
        """

    @POST(API_PROJECT_ANALYSES_DELETE_ENDPOINT)
    def delete_project_analysis(self, analysis):
        """
        SINCE 6.3
        Delete a project analysis.

        :param analysis: Analysis key
        :return:
        """

    @POST(API_PROJECT_ANALYSES_DELETE_EVENT_ENDPOINT)
    def delete_project_analysis_event(self, event):
        """
        SINCE 6.3
        Delete a project analysis event.Only event of category 'VERSION' and 'OTHER' can be deleted.

        :param event: Event key
        :return:
        """

    @PAGES_GET(API_PROJECT_ANALYSES_SEARCH_ENDPOINT, item="analyses")
    def search_project_analyses_and_events(
        self, project, branch=None, category=None, from_date=None, to_date=None
    ):
        """
        SINCE 6.3
        Search a project analyses and attached events.

        :param project: Project key
        :param branch: Branch key
        :param category: Event category. Filter analyses that have at least one event of the category specified.
          Possible values are for:
            * VERSION
            * OTHER
            * QUALITY_PROFILE
            * QUALITY_GATE
            * DEFINITION_CHANGE
        :param from_date: Filter analyses created after the given date (inclusive).
          Either a date (server timezone) or datetime can be provided
        :param to_date: Filter analyses created before the given date (inclusive).
          Either a date (server timezone) or datetime can be provided
        :return:
        """

    @POST(API_PROJECT_ANALYSES_SET_BASELINE_ENDPOINT)
    def set_analysis_as_baseline_on_project(self, project, analysis, branch=None):
        """
        SINCE 7.7
        DEPRECATED SINCE 8.0
        Set an analysis as the baseline of the New Code Period on a project or a long-lived branch.
        This manually set baseline overrides the `sonar.leak.period` setting.

        :param project: Project key
        :param analysis: Analysis key
        :param branch: Branch key
        :return:
        """

    @POST(API_PROJECT_ANALYSES_UNSET_BASELINE_ENDPOINT)
    def unset_baseline_on_project(self, project, branch=None):
        """
        SINCE 7.7
        DEPRECATED SINCE 8.0
        Unset any manually-set New Code Period baseline on a project or a long-lived branch.
        Unsetting a manual baseline restores the use of the `sonar.leak.period` setting.

        :param project: Project key
        :param branch: Branch key
        :return:
        """

    @POST(API_PROJECT_ANALYSES_UPDATE_EVENT_ENDPOINT)
    def update_project_analysis_event(self, event, name):
        """
        SINCE 6.3
        Update a project analysis event.
        Only events of category 'VERSION' and 'OTHER' can be updated.

        :param event: Event key
        :param name: New name
        :return: request response
        """
