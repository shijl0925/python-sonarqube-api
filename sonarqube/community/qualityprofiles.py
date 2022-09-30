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
    API_QUALITYPROFILES_RESTORE_ENDPOINT,
    API_QUALITYPROFILES_ADD_GROUP_ENDPOINT,
)
from sonarqube.utils.common import GET, POST, PAGES_GET


class SonarQubeQualityProfiles(RestClient):
    """
    SonarQube quality profiles Operations
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeQualityProfiles, self).__init__(**kwargs)

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
                "{}={}".format(k, v) for k, v in sorted(params.items()) if v
            )
            if params:
                data["params"] = params

        return self._post(API_QUALITYPROFILES_ACTIVATE_RULE_ENDPOINT, params=data)

    @POST(API_QUALITYPROFILES_ADD_GROUP_ENDPOINT)
    def add_group_to_quality_profile(self, group, language, qualityProfile):
        """
        SINCE 6.6
        Allow a group of users to edit a Quality Profile.

        :param group: Group name
        :param language: Quality profile language
        :param qualityProfile: Quality Profile name
        :return:
        """

    @GET(API_QUALITYPROFILES_SEARCH_ENDPOINT)
    def search_quality_profiles(
        self, defaults="false", language=None, project=None, qualityProfile=None
    ):
        """
        SINCE 5.2
        Search quality profiles

        :param defaults: If set to true, return only the quality profiles marked as default for each language.
          Possible values are for: true or false. default value is false.
        :param language: Language key. If provided, only profiles for the given language are returned.
        :param project: Project key
        :param qualityProfile: Quality profile name
        :return:
        """

    @POST(API_QUALITYPROFILES_SET_DEFAULT_ENDPOINT)
    def set_default_quality_profile(self, language, qualityProfile):
        """
        SINCE 5.2
        Select the default profile for a given language.

        :param language: Quality profile language.
        :param qualityProfile: Quality profile name.
        :return:
        """

    @POST(API_QUALITYPROFILES_ADD_PROJECT_ENDPOINT)
    def associate_project_with_quality_profile(self, project, language, qualityProfile):
        """
        SINCE 5.2
        Associate a project with a quality profile.

        :param project: Project key.
        :param language: Quality profile language.
        :param qualityProfile: Quality profile name.
        :return:
        """

    @POST(API_QUALITYPROFILES_REMOVE_PROJECT_ENDPOINT)
    def remove_project_associate_with_quality_profile(
        self, project, language, qualityProfile
    ):
        """
        SINCE 5.2
        Remove a project's association with a quality profile.

        :param project: Project key
        :param language: Quality profile language.
        :param qualityProfile: Quality profile name.
        :return:
        """

    @GET(API_QUALITYPROFILES_BACKUP_ENDPOINT)
    def backup_quality_profile(self, language, qualityProfile):
        """
        SINCE 5.2
        Backup a quality profile in XML form. The exported profile can be restored through api/qualityprofiles/restore.

        :param language: Quality profile language.
        :param qualityProfile: Quality profile name.
        :return:
        """

    @POST(API_QUALITYPROFILES_CHANGE_PARENT_ENDPOINT)
    def change_parent_of_quality_profile(
        self, parentQualityProfile, language, qualityProfile
    ):
        """
        SINCE 5.2
        Change a quality profile's parent.

        :param parentQualityProfile: Parent quality profile name.
        :param language: Quality profile language.
        :param qualityProfile: Quality profile name.
        :return:
        """

    @PAGES_GET(API_QUALITYPROFILES_CHANGELOG_ENDPOINT, item="events")
    def get_history_of_changes_on_quality_profile(
        self, language, qualityProfile, since=None, to=None
    ):
        """
        SINCE 5.2
        Get the history of changes on a quality profile: rule activation/deactivation, change in parameters/severity.
        Events are ordered by date in descending order (most recent first).

        :param language: Quality profile language.
        :param qualityProfile: Quality profile language.
        :param since: Start date for the changelog. Either a date (server timezone) or datetime can be provided.
        :param to: End date for the changelog. Either a date (server timezone) or datetime can be provided.
        :return:
        """

    @POST(API_QUALITYPROFILES_COPY_ENDPOINT)
    def copy_quality_profile(self, fromKey, toName):
        """
        SINCE 5.2
        Copy a quality profile.

        :param fromKey: Quality profile key
        :param toName: Name for the new quality profile.
        :return: request response
        """

    @POST(API_QUALITYPROFILES_CREATE_ENDPOINT)
    def create_quality_profile(self, language, name):
        """
        SINCE 5.2
        Create a quality profile.

        :param language: Quality profile language
        :param name: Quality profile name
        :return: request response
        """

    @POST(API_QUALITYPROFILES_DEACTIVATE_RULE_ENDPOINT)
    def deactivate_rule_on_quality_profile(self, key, rule):
        """
        SINCE 4.4
        Deactivate a rule on a quality profile.

        :param key: Quality Profile key. Can be obtained through api/qualityprofiles/search
        :param rule: Rule key
        :return:
        """

    @POST(API_QUALITYPROFILES_DELETE_ENDPOINT)
    def delete_quality_profile(self, language, qualityProfile):
        """
        SINCE 5.2
        Delete a quality profile and all its descendants.
        The default quality profile cannot be deleted.

        :param language: Quality profile language.
        :param qualityProfile: Quality profile name.
        :return:
        """

    @GET(API_QUALITYPROFILES_EXPORT_ENDPOINT)
    def export_quality_profile(
        self, exporterKey=None, language=None, qualityProfile=None
    ):
        """
        SINCE 5.2
        Export a quality profile.

        :param exporterKey: Output format. If left empty, the same format as api/qualityprofiles/backup is used.
          Possible values are described by api/qualityprofiles/exporters.
          Possible values are for:
            * sonarlint-vs-vbnet
            * findbugs
            * pmd
            * sonarlint-vs-cs
            * roslyn-vbnet
            * roslyn-cs
        :param language: Quality profile language
        :param qualityProfile: Quality profile name to export. If left empty, the default profile for the language
        is exported.
        :return:
        """

    @GET(API_QUALITYPROFILES_EXPORTERS_ENDPOINT)
    def get_supported_exporters(self):
        """
        SINCE 5.2
        Lists available profile export formats.

        :return:
        """

    @GET(API_QUALITYPROFILES_IMPORTERS_ENDPOINT)
    def get_supported_importers(self):
        """
        SINCE 5.2
        List supported importers.

        :return:
        """

    @GET(API_QUALITYPROFILES_INHERITANCE_ENDPOINT)
    def show_quality_profile(self, language, qualityProfile):
        """
        SINCE 5.2
        Show a quality profile's ancestors and children.

        :param language: Quality profile language.
        :param qualityProfile: Quality profile name.
        :return:
        """

    @PAGES_GET(API_QUALITYPROFILES_PROJECTS_ENDPOINT, item="results")
    def get_projects_associate_with_quality_profile(
        self, key, q=None, selected="selected"
    ):
        """
        SINCE 5.2
        List projects with their association status regarding a quality profile

        :param key: Quality profile key
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
        SINCE 5.2
        Rename a quality profile.

        :param key: Quality profile key
        :param name: New quality profile name
        :return:
        """

    def restore_quality_profile(self, backup):
        """
        SINCE 5.2
        Restore a quality profile using an XML file. The restored profile name is taken from the backup file,
        so if a profile with the same name and language already exists, it will be overwritten.

        :param backup: A profile backup file in XML format, as generated by api/qualityprofiles/backup
          or the former api/profiles/backup.
        :return:
        """
        files = {'backup': backup}
        return self._post(API_QUALITYPROFILES_RESTORE_ENDPOINT, files=files)
