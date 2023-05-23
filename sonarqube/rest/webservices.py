#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_WEBSERVICES_LIST_ENDPOINT,
    API_WEBSERVICES_RESPONSE_EXAMPLE_ENDPOINT,
)
from sonarqube.utils.common import GET, POST


class SonarQubeWebservices(RestClient):
    """
    SonarQube webservices Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeWebservices, self).__init__(**kwargs)

    @GET(API_WEBSERVICES_LIST_ENDPOINT)
    def list_web_services(self, include_internals="false"):
        """
        SINCE 4.2
        List web services

        :param include_internals: Include web services that are implemented for internal use only.
          Their forward-compatibility is not assured. Possible values are for: true or false. default value is false.
        :return:
        """

    @POST(API_WEBSERVICES_RESPONSE_EXAMPLE_ENDPOINT)
    def web_service_response_example(self, action, controller):
        """
        SINCE 4.4
        Display web service response example

        :param action: Action of the web service
        :param controller: Controller of the web service
        :return:
        """
