#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.common import POST, GET
from sonarqube.utils.rest_client import RestClient

from sonarqube.utils.config import (
    API_VIEWS_UPDATE,  # pro
    API_VIEWS_SHOW,  # pro
    API_VIEWS_LIST,  # pro
)


class SonarQubeViews(RestClient):
    """
    Manage Portfolios
    """

    special_attributes_map = {"definition": "def"}

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeViews, self).__init__(**kwargs)

    def get(self, key):
        result = self.list()
        for view in result["views"]:
            if view["key"] == key:
                return view
    @GET(API_VIEWS_LIST)
    def list(self):
        """
        since 1.0
        List root portfolios.
        Requires authentication. Only portfolios with the admin permission are returned.

        :return:
        """
    @GET(API_VIEWS_SHOW)
    def show(self, key):
        """
        since 1.0
        Show the details of a portfolio, including its hierarchy and project selection mode.
        Authentication is required for this API endpoint

        :param key: The key of the portfolio
        :return:
        """

    @POST(API_VIEWS_UPDATE)
    def update(self, key, name, description=None):
        """
        since 1.0
        Update a portfolio.
        Requires 'Administrator' permission on the portfolio

        :param key: Key of the portfolio to update
        :param name: New name for the portfolio
        :param description: New description for the application
        :return:
        """
