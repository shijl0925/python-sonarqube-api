#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_QUALITYPROFILES_ACTIVATE_RULE_ENDPOINT,
    API_QUALITYPROFILES_SEARCH_ENDPOINT,
    API_QUALITYPROFILES_DELETE_ENDPOINT,
)
from sonarqube.utils.common import GET, POST


class SonarQubeQualityProfiles(RestClient):
    """
    SonarQube quality profiles Operations
    """

    def activate_rule_for_quality_profile(
        self, key, rule, reset=False, severity=None, **params
    ):
        """
        SINCE 4.4
        Activate a rule for a given quality profile.

        :param key: Quality Profile key.
        :param rule: Rule key
        :param reset: Reset severity and parameters of activated rule.
          Set the values defined on parent profile or from rule default values.
        :param severity: Severity. Ignored if parameter reset is true.
          Possible values are for:
            * INFO
            * MINOR
            * MAJOR
            * CRITICAL
            * BLOCKER
        :param params: customized parameters for the rule.Ignored if parameter reset is true.
        :return:
        """
        data = {"rule": rule, "key": key, "reset": reset and "true" or "false"}

        if not reset:
            # No reset, Add severity if given (if not default will be used?)
            if severity:
                data["severity"] = severity.upper()

            # Add params if we have any
            # Note: sort by key to allow checking easily
            params = ";".join(
                f"{k}={v}" for k, v in sorted(params.items()) if v
            )
            if params:
                data["params"] = params

        return self._post(API_QUALITYPROFILES_ACTIVATE_RULE_ENDPOINT, data=data)

    @GET(API_QUALITYPROFILES_SEARCH_ENDPOINT)
    def search_quality_profiles(
        self, organization=None, defaults="false", language=None, project=None, qualityProfile=None
    ):
        """
        SINCE 5.2
        Search quality profiles

        :param organization: organization key.
        :param defaults: If set to true, return only the quality profiles marked as default for each language.
          Possible values are for: true or false. default value is false.
        :param language: Language key. If provided, only profiles for the given language are returned.
        :param project: Project key
        :param qualityProfile: Quality profile name
        :return:
        """
    @POST(API_QUALITYPROFILES_DELETE_ENDPOINT)
    def delete_quality_profile(self, language, qualityProfile, organization=None):
        """
        SINCE 5.2
        Delete a quality profile and all its descendants.
        The default quality profile cannot be deleted.

        :param language: Quality profile language.
        :param qualityProfile: Quality profile name.
        :param organization: Organization key.
        :return:
        """
