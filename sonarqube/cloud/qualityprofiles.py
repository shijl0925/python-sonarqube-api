#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.community.qualityprofiles import SonarQubeQualityProfiles
from sonarqube.utils.config import (
    API_QUALITYPROFILES_SEARCH_ENDPOINT,
    API_QUALITYPROFILES_DELETE_ENDPOINT,
    API_QUALITYPROFILES_SET_DEFAULT_ENDPOINT,
    API_QUALITYPROFILES_ADD_PROJECT_ENDPOINT,
    API_QUALITYPROFILES_BACKUP_ENDPOINT,
    API_QUALITYPROFILES_CHANGE_PARENT_ENDPOINT,
    API_QUALITYPROFILES_CHANGELOG_ENDPOINT,
    API_QUALITYPROFILES_CREATE_ENDPOINT,
    API_QUALITYPROFILES_EXPORT_ENDPOINT,
    API_QUALITYPROFILES_INHERITANCE_ENDPOINT,
    API_QUALITYPROFILES_REMOVE_PROJECT_ENDPOINT,
    API_QUALITYPROFILES_RESTORE_ENDPOINT
)


class SonarCloudQualityProfiles(SonarQubeQualityProfiles):
    """
    SonarCloud quality profiles Operations
    """

    def search_quality_profiles(self, organization, defaults=False, language=None, project_key=None, profile_name=None):
        """
        Search quality profiles

        :param organization: organization key.
        :param defaults: If set to true, return only the quality profiles marked as default for each language.
          Possible values are for: True or False. default value is False.
        :param language: Language key. If provided, only profiles for the given language are returned.
        :param project_key: Project key
        :param profile_name: Quality profile name
        :return:
        """
        params = {
            'organization': organization,
            'defaults': defaults and 'true' or 'false'
        }

        if language:
            params.update({'language': language})

        if project_key:
            params.update({'project': project_key})

        if profile_name:
            params.update({'qualityProfile': profile_name})

        res = self.get(API_QUALITYPROFILES_SEARCH_ENDPOINT, params=params)
        response = res.json()
        return response['profiles']

    def set_default_quality_profile(self, language, profile_name, organization):
        """
        Select the default profile for a given language.

        :param language: Quality profile language.
        :param profile_name: Quality profile name.
        :param organization: organization key.
        :return:
        """
        params = {
            'language': language,
            'qualityProfile': profile_name,
            'organization': organization
        }

        self.post(API_QUALITYPROFILES_SET_DEFAULT_ENDPOINT, params=params)

    def associate_project_with_quality_profile(self, project, language, profile_name, organization):
        """
        Associate a project with a quality profile.

        :param project: Project key.
        :param language: Quality profile language.
        :param profile_name: Quality profile name.
        :param organization: Organization key.

        :return:
        """
        params = {
            'project': project,
            'language': language,
            'qualityProfile': profile_name,
            'organization': organization
        }

        self.post(API_QUALITYPROFILES_ADD_PROJECT_ENDPOINT, params=params)

    def remove_project_associate_with_quality_profile(self, project, language, profile_name, organization):
        """
        Remove a project's association with a quality profile.

        :param project: Project key
        :param language: Quality profile language.
        :param profile_name: Quality profile name.
        :param organization: Organization key.
        :return:
        """
        params = {
            'project': project,
            'language': language,
            'qualityProfile': profile_name,
            'organization': organization
        }

        self.post(API_QUALITYPROFILES_REMOVE_PROJECT_ENDPOINT, params=params)

    def backup_quality_profile(self, language, profile_name, organization):
        """
        Backup a quality profile in XML form. The exported profile can be restored through api/qualityprofiles/restore.

        :param language: Quality profile language.
        :param profile_name: Quality profile name.
        :param organization: Organization key.
        :return:
        """
        params = {
            'language': language,
            'qualityProfile': profile_name,
            'organization': organization
        }

        resp = self.get(API_QUALITYPROFILES_BACKUP_ENDPOINT, params=params)
        return resp.text

    def change_parent_of_quality_profile(self, parent_profile_name, language, profile_name, organization):
        """
        Change a quality profile's parent.

        :param parent_profile_name: Parent quality profile name.
        :param language: Quality profile language.
        :param profile_name: Quality profile name.
        :param organization: Organization key.
        :return:
        """
        params = {
            'parentQualityProfile': parent_profile_name,
            'language': language,
            'qualityProfile': profile_name,
            'organization': organization
        }

        self.post(API_QUALITYPROFILES_CHANGE_PARENT_ENDPOINT, params=params)

    def get_history_of_changes_on_quality_profile(self, language, profile_name, organization, since_data=None, to_data=None):
        """
        Get the history of changes on a quality profile: rule activation/deactivation, change in parameters/severity.
        Events are ordered by date in descending order (most recent first).

        :param language: Quality profile language.
        :param profile_name: Quality profile language.
        :param organization: Organization key.
        :param since_data: Start date for the changelog. Either a date (server timezone) or datetime can be provided.
        :param to_data: End date for the changelog. Either a date (server timezone) or datetime can be provided.
        :return:
        """
        params = {
            'language': language,
            'qualityProfile': profile_name,
            'organization': organization
        }

        if since_data:
            params.update({'since': since_data})

        if to_data:
            params.update({'to': to_data})

        page_num = 1
        page_size = 1
        total = 2

        while page_num * page_size < total:
            resp = self.get(API_QUALITYPROFILES_CHANGELOG_ENDPOINT, params=params)
            response = resp.json()

            page_num = response['p']
            page_size = response['ps']
            total = response['total']

            params['p'] = page_num + 1

            for event in response['events']:
                yield event

    def create_quality_profile(self, language, profile_name, organization):
        """
        Create a quality profile.

        :param language: Quality profile language
        :param profile_name: Quality profile name
        :pram organization: Organization key.

        :return: request response
        """
        params = {
            'language': language,
            'name': profile_name,
            'organization': organization
        }

        return self.post(API_QUALITYPROFILES_CREATE_ENDPOINT, params=params)

    def delete_quality_profile(self, language, profile_name, organization):
        """
        Delete a quality profile and all its descendants.
        The default quality profile cannot be deleted.

        :param language: Quality profile language.
        :param profile_name: Quality profile name.
        :param organization: Organization key.
        :return:
        """
        params = {
            'language': language,
            'qualityProfile': profile_name,
            'organization': organization
        }

        self.post(API_QUALITYPROFILES_DELETE_ENDPOINT, params=params)

    def export_quality_profile(self, organization, exporter_key=None, language=None, profile_name=None):
        """
        Export a quality profile.

        :param organization: Organization key.
        :param exporter_key: Output format. If left empty, the same format as api/qualityprofiles/backup is used.
          Possible values are described by api/qualityprofiles/exporters.
          Possible values are for:
            * sonarlint-vs-vbnet
            * findbugs
            * pmd
            * sonarlint-vs-cs
            * roslyn-vbnet
            * roslyn-cs
        :param language: Quality profile language
        :param profile_name: Quality profile name to export. If left empty, the default profile for the language
        is exported.
        :return:
        """
        params = {'organization': organization}

        if exporter_key:
            params.update({'exporterKey': exporter_key})

        if language:
            params.update({'language': language})

        if profile_name:
            params.update({'qualityProfile': profile_name})

        res = self.get(API_QUALITYPROFILES_EXPORT_ENDPOINT, params=params)
        return res.text

    def show_quality_profile(self, language, profile_name, organization):
        """
        Show a quality profile's ancestors and children.

        :param language: Quality profile language.
        :param profile_name: Quality profile name.
        :param organization: Organization key.

        :return:
        """
        params = {
            'language': language,
            'qualityProfile': profile_name,
            'organization': organization
        }

        res = self.get(API_QUALITYPROFILES_INHERITANCE_ENDPOINT, params=params)
        return res.json()

    def restore_quality_profile(self, backup, organization):
        """
        Restore a quality profile using an XML file. The restored profile name is taken from the backup file,
        so if a profile with the same name and language already exists, it will be overwritten.

        :param backup: A profile backup file in XML format, as generated by api/qualityprofiles/backup
          or the former api/profiles/backup.
        :param organization: organization key.

        :return:
        """
        params = {'backup': backup, 'organization': organization}

        self.post(API_QUALITYPROFILES_RESTORE_ENDPOINT, params=params)
