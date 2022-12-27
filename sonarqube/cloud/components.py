#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.community.components import SonarQubeComponents
from sonarqube.utils.config import API_COMPONTENTS_SEARCH_ENDPOINT
from sonarqube.utils.common import GET


class SonarCloudComponents(SonarQubeComponents):
    """
    SonarCloud components Operations
    """

    @GET(API_COMPONTENTS_SEARCH_ENDPOINT)
    def search_components(self, organization, qualifiers, language=None, q=None, p=None, ps=None):
        """
        Search for components

        :param organization: Organization key
        :param qualifiers: Comma-separated list of component qualifiers. Filter the results with
          the specified qualifiers. Possible values are:

          * BRC - Sub-projects
          * DIR - Directories
          * FIL - Files
          * TRK - Projects
          * UTS - Test Files

        :param language: Language key. If provided, only components for the given language are returned.
        :param q: Limit search to:

          * component names that contain the supplied string
          * component keys that are exactly the same as the supplied string
        :param p: page number.
        :param ps: Page size. Must be greater than 0 and less or equal than 500

        :return:
        """
