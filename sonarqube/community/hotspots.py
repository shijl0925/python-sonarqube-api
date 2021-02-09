#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import API_HOTSPOTS_SHOW_ENDPOINT
from sonarqube.utils.common import GET


class SonarQubeHotspots(RestClient):
    """
    SonarQube Security Hotspots Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeHotspots, self).__init__(**kwargs)

    @GET(API_HOTSPOTS_SHOW_ENDPOINT)
    def show(self, hotspot):
        """
        SINCE 8.1
        Provides the details of a Security Hotspot.

        :param hotspot: Key of the Security Hotspot
        :return:
        """