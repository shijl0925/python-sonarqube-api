#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_MEASURES_COMPONENT_ENDPOINT,
    API_MEASURES_COMPONENT_TREE_ENDPOINT,
    API_MEASURES_SEARCH_HISTORY_ENDPOINT,
)
from sonarqube.utils.common import GET, PAGES_GET


class SonarQubeMeasures(RestClient):
    """
    SonarQube measures Operations
    """

    special_attributes_map = {"from_date": "from", "to_date": "to"}

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeMeasures, self).__init__(**kwargs)

    @GET(API_MEASURES_COMPONENT_ENDPOINT)
    def get_component_with_specified_measures(
        self,
        component,
        metricKeys,
        branch=None,
        pullRequest=None,
        additionalFields=None,
    ):
        """
        SINCE 5.4
        Return component with specified measures.

        :param component: Component key
        :param branch: Branch key.
        :param pullRequest: Pull request id.
        :param additionalFields: Comma-separated list of additional fields that can be returned in the response.
          Possible values are for: metrics,periods
        :param metricKeys: Comma-separated list of metric keys. Possible values are for: ncloc,complexity,violations
        :return:
        """

    @PAGES_GET(API_MEASURES_COMPONENT_TREE_ENDPOINT, item="components")
    def get_component_tree_with_specified_measures(
        self,
        component,
        metricKeys,
        branch=None,
        pullRequest=None,
        asc="true",
        additionalFields=None,
        metricPeriodSort=None,
        metricSort=None,
        metricSortFilter="all",
        ps=None,
        q=None,
        s="name",
        qualifiers=None,
        strategy="all",
    ):
        """
        SINCE 5.4
        Navigate through components based on the chosen strategy with specified measures. The baseComponentId or
        the component parameter must be provided.

        :param component: Component key.
        :param branch: Branch key.
        :param pullRequest: Pull request id.
        :param metricKeys: Comma-separated list of metric keys. Possible values are for: ncloc,complexity,violations
        :param additionalFields: Comma-separated list of additional fields that can be returned in the response.
            Possible values are for: metrics,periods
        :param asc: Ascending sort, Possible values are for: true, false, yes, no. default value is true.
        :param metricPeriodSort: Sort measures by leak period or not ?. The 's' parameter must contain
            the 'metricPeriod' value
        :param metricSort: Metric key to sort by. The 's' parameter must contain the 'metric' or 'metricPeriod' value.
            It must be part of the 'metricKeys' parameter
        :param metricSortFilter: Filter components. Sort must be on a metric. Possible values are:

            * all: return all components
            * withMeasuresOnly: filter out components that do not have a measure on the sorted metric

            default value is all.
        :param ps: Page size. Must be greater than 0 and less or equal than 500
        :param q: Limit search to:

            * component names that contain the supplied string
            * component keys that are exactly the same as the supplied string

        :param qualifiers:Comma-separated list of component qualifiers. Filter the results with
            the specified qualifiers. Possible values are:

            * BRC - Sub-projects
            * DIR - Directories
            * FIL - Files
            * TRK - Projects
            * UTS - Test Files

        :param s: Comma-separated list of sort fields,Possible values are for: name, path, qualifier, metric, metricPeriod.
            and default value is name
        :param strategy: Strategy to search for base component descendants:

            * children: return the children components of the base component. Grandchildren components are not returned
            * all: return all the descendants components of the base component. Grandchildren are returned.
            * leaves: return all the descendant components (files, in general) which don't have other children.
              They are the leaves of the component tree.

            default value is all.

        :return:
        """

    @PAGES_GET(API_MEASURES_SEARCH_HISTORY_ENDPOINT, item="measures")
    def search_measures_history(
        self,
        component,
        metrics,
        branch=None,
        pullRequest=None,
        from_date=None,
        to_date=None,
    ):
        """
        SINCE 6.3
        Search measures history of a component

        :param component: Component key.
        :param branch: Branch key.
        :param pullRequest: Pull request id.
        :param metrics: Comma-separated list of metric keys.Possible values are for: ncloc,coverage,new_violations
        :param from_date: Filter measures created after the given date (inclusive).
          Either a date (server timezone) or datetime can be provided
        :param to_date: Filter measures created before the given date (inclusive).
          Either a date (server timezone) or datetime can be provided
        :return:
        """
