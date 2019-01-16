#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .config import *

class SonarQubeQualityprofiles(object):
    def __init__(self, sonarqube):
        self.sonarqube = sonarqube

    def activate_rule(self, key, profile_key, reset=False, severity=None,
                      **params):
        """
        Activate a rule for a given quality profile.
        :param key: key of the rule
        :param profile_key: key of the profile
        :param reset: reset severity and params to default
        :param severity: severity of rule for given profile
        :param params: customized parameters for the rule
        :return: request response
        """
        # Build main data to post
        data = {
            'rule': key,
            'key': profile_key,
            'reset': reset and 'true' or 'false'
        }

        if not reset:
            # No reset, Add severity if given (if not default will be used?)
            if severity:
                data['severity'] = severity.upper()

            # Add params if we have any
            # Note: sort by key to allow checking easily
            params = ';'.join('{}={}'.format(k, v) for k, v in sorted(params.items()) if v)
            if params:
                data['params'] = params

        self.sonarqube._make_call('post', RULES_QUALITYPROFILES_ACTIVATE_RULE_ENDPOINT, **data)

    def get_qualityprofiles(self, **kwargs):
        """
        :param kwargs:
        :return:
        """
        res = self.sonarqube._make_call('get', RULES_QUALITYPROFILES_SEARCH_ENDPOINT, **kwargs)
        return res.json()['profiles']

    def delete_qualityprofile(self, language, name):
        """
        Delete a quality profile and all its descendants.
        The default quality profile cannot be deleted.
        :param name:
        :return:
        """
        params = {'qualityProfile': name, 'language': language}
        self.sonarqube._make_call('post', RULES_QUALITYPROFILES_DELETE_ENDPOINT, **params)

    def set_default_qualityprofile(self, language, name):
        """
        Select the default profile for a given language.
        :param name:
        :return:
        """
        params = {'qualityProfile': name, 'language': language}
        self.sonarqube._make_call('post', RULES_QUALITYPROFILES_SET_DEFAULT_ENDPOINT, **params)

