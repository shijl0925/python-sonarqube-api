#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.community.hotspots import SonarQubeHotspots
from sonarqube.utils.config import (
    API_HOTSPOTS_CHANGE_STATUS_ENDPOINT,
)
from sonarqube.utils.common import POST


class SonarEnterpriseHotspots(SonarQubeHotspots):
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