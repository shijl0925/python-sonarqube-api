#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.utils.rest_client import RestClient
from sonarqube.utils.config import (
    API_QUALITYPROFILES_ACTIVATE_RULE_ENDPOINT,
    API_QUALITYPROFILES_SEARCH_ENDPOINT,
    API_QUALITYPROFILES_DELETE_ENDPOINT,
    API_QUALITYPROFILES_SET_DEFAULT_ENDPOINT,
    API_QUALITYPROFILES_ADD_PROJECT_ENDPOINT,
    API_QUALITYPROFILES_BACKUP_ENDPOINT,
    API_QUALITYPROFILES_CHANGE_PARENT_ENDPOINT,
    API_QUALITYPROFILES_CHANGELOG_ENDPOINT,
    API_QUALITYPROFILES_COPY_ENDPOINT,
    API_QUALITYPROFILES_CREATE_ENDPOINT,
    API_QUALITYPROFILES_DEACTIVATE_RULE_ENDPOINT,
    API_QUALITYPROFILES_EXPORT_ENDPOINT,
    API_QUALITYPROFILES_EXPORTERS_ENDPOINT,
    API_QUALITYPROFILES_IMPORTERS_ENDPOINT,
    API_QUALITYPROFILES_INHERITANCE_ENDPOINT,
    API_QUALITYPROFILES_REMOVE_PROJECT_ENDPOINT,
    API_QUALITYPROFILES_PROJECTS_ENDPOINT,
    API_QUALITYPROFILES_RENAME_ENDPOINT,
    API_QUALITYPROFILES_RESTORE_ENDPOINT
)
from sonarqube.utils.common import GET, POST, PAGE_GET


class SonarQubeQualityProfiles(RestClient):
    """
    SonarQube quality profiles Operations
    """
    special_attributes_map = {
        'profile_name': 'qualityProfile',
        'parent_profile_name': 'parentQualityProfile',
        'previous_profile_key': 'fromKey',
        'new_profile_name': 'toName',
        'profile_key': 'key',
        'rule_key': 'rule',
        'exporter_key': 'exporterKey',
        'since_data': 'since',
        'to_date': 'to'
    }

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeQualityProfiles, self).__init__(**kwargs)

    def activate_rule_for_quality_profile(self, profile_key, rule_key, reset=False, severity=None, **params):
        """
        Activate a rule for a given quality profile.

        :param profile_key: Quality Profile key.
        :param rule_key: Rule key
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
        data = {
            'rule': rule_key,
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

        self.post(API_QUALITYPROFILES_ACTIVATE_RULE_ENDPOINT, params=data)

    @GET(API_QUALITYPROFILES_SEARCH_ENDPOINT)
    def search_quality_profiles(self, defaults='false', language=None, project_key=None, profile_name=None):
        """
        Search quality profiles

        :param defaults: If set to true, return only the quality profiles marked as default for each language.
          Possible values are for: true or false. default value is false.
        :param language: Language key. If provided, only profiles for the given language are returned.
        :param project_key: Project key
        :param profile_name: Quality profile name
        :return:
        """

    @POST(API_QUALITYPROFILES_SET_DEFAULT_ENDPOINT)
    def set_default_quality_profile(self, language, profile_name):
        """
        Select the default profile for a given language.

        :param language: Quality profile language.
        :param profile_name: Quality profile name.
        :return:
        """
    @POST(API_QUALITYPROFILES_ADD_PROJECT_ENDPOINT)
    def associate_project_with_quality_profile(self, project, language, profile_name):
        """
        Associate a project with a quality profile.

        :param project: Project key.
        :param language: Quality profile language.
        :param profile_name: Quality profile name.
        :return:
        """

    @POST(API_QUALITYPROFILES_REMOVE_PROJECT_ENDPOINT)
    def remove_project_associate_with_quality_profile(self, project, language, profile_name):
        """
        Remove a project's association with a quality profile.

        :param project: Project key
        :param language: Quality profile language.
        :param profile_name: Quality profile name.
        :return:
        """

    @GET(API_QUALITYPROFILES_BACKUP_ENDPOINT)
    def backup_quality_profile(self, language, profile_name):
        """
        Backup a quality profile in XML form. The exported profile can be restored through api/qualityprofiles/restore.

        :param language: Quality profile language.
        :param profile_name: Quality profile name.
        :return:
        """

    @POST(API_QUALITYPROFILES_CHANGE_PARENT_ENDPOINT)
    def change_parent_of_quality_profile(self, parent_profile_name, language, profile_name):
        """
        Change a quality profile's parent.

        :param parent_profile_name: Parent quality profile name.
        :param language: Quality profile language.
        :param profile_name: Quality profile name.
        :return:
        """

    @PAGE_GET(API_QUALITYPROFILES_CHANGELOG_ENDPOINT, item='events')
    def get_history_of_changes_on_quality_profile(self, language, profile_name, since_data=None, to_data=None):
        """
        Get the history of changes on a quality profile: rule activation/deactivation, change in parameters/severity.
        Events are ordered by date in descending order (most recent first).

        :param language: Quality profile language.
        :param profile_name: Quality profile language.
        :param since_data: Start date for the changelog. Either a date (server timezone) or datetime can be provided.
        :param to_data: End date for the changelog. Either a date (server timezone) or datetime can be provided.
        :return:
        """

    @POST(API_QUALITYPROFILES_COPY_ENDPOINT)
    def copy_quality_profile(self, previous_profile_key, new_profile_name):
        """
        Copy a quality profile.

        :param previous_profile_key: Quality profile key
        :param new_profile_name: Name for the new quality profile.
        :return: request response
        """

    @POST(API_QUALITYPROFILES_CREATE_ENDPOINT)
    def create_quality_profile(self, language, name, **kwargs):
        """
        Create a quality profile.

        :param language: Quality profile language
        :param name: Quality profile name
        :param kwargs:
        :return: request response
        """

    @POST(API_QUALITYPROFILES_DEACTIVATE_RULE_ENDPOINT)
    def deactivate_rule_on_quality_profile(self, profile_key, rule_key):
        """
        Deactivate a rule on a quality profile.

        :param profile_key: Quality Profile key. Can be obtained through api/qualityprofiles/search
        :param rule_key: Rule key
        :return:
        """

    @POST(API_QUALITYPROFILES_DELETE_ENDPOINT)
    def delete_quality_profile(self, language, profile_name):
        """
        Delete a quality profile and all its descendants.
        The default quality profile cannot be deleted.

        :param language: Quality profile language.
        :param profile_name: Quality profile name.
        :return:
        """

    @GET(API_QUALITYPROFILES_EXPORT_ENDPOINT)
    def export_quality_profile(self, exporter_key=None, language=None, profile_name=None):
        """
        Export a quality profile.

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

    @GET(API_QUALITYPROFILES_EXPORTERS_ENDPOINT)
    def get_supported_exporters(self):
        """
        Lists available profile export formats.

        :return:
        """

    @GET(API_QUALITYPROFILES_IMPORTERS_ENDPOINT)
    def get_supported_importers(self):
        """
        List supported importers.

        :return:
        """

    @GET(API_QUALITYPROFILES_INHERITANCE_ENDPOINT)
    def show_quality_profile(self, language, profile_name):
        """
        Show a quality profile's ancestors and children.

        :param language: Quality profile language.
        :param profile_name: Quality profile name.
        :return:
        """

    @PAGE_GET(API_QUALITYPROFILES_PROJECTS_ENDPOINT, item='results')
    def get_projects_associate_with_quality_profile(self, profile_key, q=None, selected="selected"):
        """
        List projects with their association status regarding a quality profile

        :param profile_key: Quality profile key
        :param q: Limit search to projects that contain the supplied string.
        :param selected: Depending on the value, show only selected items (selected=selected),
          deselected items (selected=deselected), or all items with their selection status (selected=all).
          Possible values are for:
            * all
            * deselected
            * selected
          default value is selected.
        :return:
        """

    @POST(API_QUALITYPROFILES_RENAME_ENDPOINT)
    def rename_quality_profile(self, key, name):
        """
        Rename a quality profile.

        :param key: Quality profile key
        :param name: New quality profile name
        :return:
        """

    @POST(API_QUALITYPROFILES_RESTORE_ENDPOINT)
    def restore_quality_profile(self, backup):
        """
        Restore a quality profile using an XML file. The restored profile name is taken from the backup file,
        so if a profile with the same name and language already exists, it will be overwritten.

        :param backup: A profile backup file in XML format, as generated by api/qualityprofiles/backup
          or the former api/profiles/backup.
        :return:
        """
