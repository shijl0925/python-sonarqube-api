#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_HOTSPOTS_SHOW_ENDPOINT,
    API_HOTSPOTS_SEARCH_ENDPOINT,
)
from sonarqube.utils.common import GET, PAGES_GET


class SonarQubeHotspots(RestClient):
    """
    SonarQube Security Hotspots Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeHotspots, self).__init__(**kwargs)

    @PAGES_GET(API_HOTSPOTS_SEARCH_ENDPOINT, item="hotspots")
    def search_hotspots(
        self,
        branch=None,
        hotspots=None,
        onlyMine=None,
        projectKey=None,
        ps=None,
        pullRequest=None,
        resolution=None,
        sinceLeakPeriod=None,
        status=None,
    ):
        """
        SINCE 8.1
        Search for security hotspots.

        :param branch: Branch key. Not available in the community edition.
        :param hotspots: Comma-separated list of Security Hotspot keys. This
            parameter is required unless projectKey is provided.
        :param onlyMine: If 'projectKey' is provided, returns only Security
            Hotspots assigned to the current user. Possible values are

                * true
                * false
                * yes
                * no

        :param projectKey: Key of the project or application. This parameter is
            required unless hotspots is provided.
        :param ps: Page size. Must be greater than 0.
        :param pullRequest: Pull request id. Not available in the community
            edition.
        :param resolution: If 'projectKey' is provided and if status is
            'REVIEWED', only Security Hotspots with the specified resolution
            are returned. Possible values are

                * FIXED
                * SAFE

        :param sinceLeakPeriod: If '%s' is provided, only Security Hotspots
            created since the leak period are returned. Possible values are

                * true
                * false
                * yes
                * no

        :param status: If 'projectKey' is provided, only Security Hotspots with
            the specified status are returned. Possible values are

                * TO_REVIEW
                * REVIEWED

        """

    @GET(API_HOTSPOTS_SHOW_ENDPOINT)
    def show(self, hotspot):
        """
        SINCE 8.1
        Provides the details of a Security Hotspot.

        :param hotspot: Key of the Security Hotspot
        :return:
        """
