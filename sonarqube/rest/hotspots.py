#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_HOTSPOTS_SHOW_ENDPOINT,
    API_HOTSPOTS_SEARCH_ENDPOINT,
    API_HOTSPOTS_CHANGE_STATUS_ENDPOINT  # pro
)
from sonarqube.utils.common import GET, POST


class SonarQubeHotspots(RestClient):
    """
    SonarQube Security Hotspots Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeHotspots, self).__init__(**kwargs)

    @GET(API_HOTSPOTS_SEARCH_ENDPOINT)
    def search_hotspots(
        self,
        branch=None,
        hotspots=None,
        onlyMine=None,
        projectKey=None,
        p=None,
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
        :param p: page number.
        :param ps: Page size. Must be greater than 0 and less or equal than 500
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

    @POST(API_HOTSPOTS_CHANGE_STATUS_ENDPOINT)
    def change_hotspots_status(self, hotspot, status, comment=None, resolution=None):
        """
        since 8.1
        Change the status of a Security Hotpot.
        Requires the 'Administer Security Hotspot' permission.

        :param hotspot: Key of the Security Hotspot
        :param status: New status of the Security Hotspot.
        :param comment: Comment text.
        :param resolution: Resolution of the Security Hotspot when new status is REVIEWED, otherwise must not be set.
        :return:
        """