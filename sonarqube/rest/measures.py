#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_MEASURES_COMPONENT_ENDPOINT,
)
from sonarqube.utils.common import GET


class SonarQubeMeasures(RestClient):
    """
    SonarQube measures Operations
    """

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
