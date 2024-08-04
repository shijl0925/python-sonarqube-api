#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.common import POST
from sonarqube.utils.rest_client import RestClient

from sonarqube.utils.config import API_EDITIONS_SET_LICENSE_ENDPOINT


class SonarQubeEditions(RestClient):
    """
    Manage SonarSource commercial editions
    """

    @POST(API_EDITIONS_SET_LICENSE_ENDPOINT)
    def set_license(self, license):
        """
        since 7.2
        Set the license for enabling features of commercial editions.
        Require 'Administer System' permission.

        :param license:
        :return:
        """
