#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_PROJECT_ANALYSES_DELETE_ENDPOINT,
    API_PROJECT_ANALYSES_SEARCH_ENDPOINT,
)
from sonarqube.utils.common import GET, POST


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

    @POST(API_PROJECT_ANALYSES_DELETE_ENDPOINT)
    def delete_project_analysis(self, analysis):
        """
        SINCE 6.3
        Delete a project analysis.

        :param analysis: Analysis key
        :return:
        """

    @GET(API_PROJECT_ANALYSES_SEARCH_ENDPOINT)
    def search_project_analyses_and_events(
        self, project, branch=None, category=None, from_date=None, to_date=None, p=None, ps=None
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
        :param p: page number.
        :param ps: Page size. Must be greater than 0 and less or equal than 500
        :return:
        """