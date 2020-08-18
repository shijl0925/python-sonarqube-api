#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sonarqube.config import (
    API_QUALITYPROFILES_ACTIVATE_RULE_ENDPOINT,
    API_QUALITYPROFILES_SEARCH_ENDPOINT,
    API_QUALITYPROFILES_DELETE_ENDPOINT,
    API_QUALITYPROFILES_SET_DEFAULT_ENDPOINT,
    API_QUALITYPROFILES_ADD_PROJECT_ENDPOINT,
    API_QUALITYPROFILES_REMOVE_PROJECT_ENDPOINT
)


class SonarQubeQualityprofiles:
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

        self.sonarqube.make_call('post', API_QUALITYPROFILES_ACTIVATE_RULE_ENDPOINT, **data)

    def search_qualityprofiles(self, defaults=None, language=None, project_key=None, name=None):
        """
        Search quality profiles
        :param defaults:
        :param language:
        :param project_key:
        :param name:
        :return:
        """
        params = {}
        if defaults:
            params.update({'defaults': defaults})

        if language:
            params.update({'language': language})

        if project_key:
            params.update({'project': project_key})

        if name:
            params.update({'qualityProfile': name})

        res = self.sonarqube.make_call('get', API_QUALITYPROFILES_SEARCH_ENDPOINT, **params)
        data = res.json()
        return data['profiles']

    def delete_qualityprofile(self, language, name):
        """
        Delete a quality profile and all its descendants.
        The default quality profile cannot be deleted.
        :param name:
        :return:
        """
        params = {'qualityProfile': name, 'language': language}
        self.sonarqube.make_call('post', API_QUALITYPROFILES_DELETE_ENDPOINT, **params)

    def set_default_qualityprofile(self, language, name):
        """
        Select the default profile for a given language.
        :param name:
        :return:
        """
        params = {'qualityProfile': name, 'language': language}
        self.sonarqube.make_call('post', API_QUALITYPROFILES_SET_DEFAULT_ENDPOINT, **params)

    def associate_project_with_quality_profile(self, project, name, language):
        """
        Associate a project with a quality profile.
        :param project:
        :param name:
        :param language:
        :return:
        """
        params = {'qualityProfile': name, 'language': language, 'project': project}
        self.sonarqube.make_call('post', API_QUALITYPROFILES_ADD_PROJECT_ENDPOINT, **params)

    def remove_project_associate_with_quality_profile(self, project, name, language):
        """
        Remove a project's association with a quality profile.
        :param project:
        :param name:
        :param language:
        :return:
        """
        params = {'qualityProfile': name, 'language': language, 'project': project}
        self.sonarqube.make_call('post', API_QUALITYPROFILES_REMOVE_PROJECT_ENDPOINT, **params)
