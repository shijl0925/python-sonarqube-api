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
    API_QUALITYPROFILES_RESTORE_ENDPOINT,
)
from sonarqube.utils.common import GET, POST, PAGES_GET


class SonarCloudQualityProfiles(SonarQubeQualityProfiles):
    """
    SonarCloud quality profiles Operations
    """

    @GET(API_QUALITYPROFILES_SEARCH_ENDPOINT)
    def search_quality_profiles(
        self,
        organization,
        defaults="false",
        language=None,
        project=None,
        qualityProfile=None,
    ):
        """
        Search quality profiles

        :param organization: organization key.
        :param defaults: If set to true, return only the quality profiles marked as default for each language.
          Possible values are for: true or false. default value is false.
        :param language: Language key. If provided, only profiles for the given language are returned.
        :param project: Project key
        :param qualityProfile: Quality profile name
        :return:
        """

    @POST(API_QUALITYPROFILES_SET_DEFAULT_ENDPOINT)
    def set_default_quality_profile(self, language, qualityProfile, organization):
        """
        Select the default profile for a given language.

        :param language: Quality profile language.
        :param qualityProfile: Quality profile name.
        :param organization: organization key.
        :return:
        """

    @POST(API_QUALITYPROFILES_ADD_PROJECT_ENDPOINT)
    def associate_project_with_quality_profile(
        self, project, language, qualityProfile, organization
    ):
        """
        Associate a project with a quality profile.

        :param project: Project key.
        :param language: Quality profile language.
        :param qualityProfile: Quality profile name.
        :param organization: Organization key.

        :return:
        """

    @POST(API_QUALITYPROFILES_REMOVE_PROJECT_ENDPOINT)
    def remove_project_associate_with_quality_profile(
        self, project, language, qualityProfile, organization
    ):
        """
        Remove a project's association with a quality profile.

        :param project: Project key
        :param language: Quality profile language.
        :param qualityProfile: Quality profile name.
        :param organization: Organization key.
        :return:
        """

    @GET(API_QUALITYPROFILES_BACKUP_ENDPOINT)
    def backup_quality_profile(self, language, qualityProfile, organization):
        """
        Backup a quality profile in XML form. The exported profile can be restored through api/qualityprofiles/restore.

        :param language: Quality profile language.
        :param qualityProfile: Quality profile name.
        :param organization: Organization key.
        :return:
        """

    @POST(API_QUALITYPROFILES_CHANGE_PARENT_ENDPOINT)
    def change_parent_of_quality_profile(
        self, parentQualityProfile, language, qualityProfile, organization
    ):
        """
        Change a quality profile's parent.

        :param parentQualityProfile: Parent quality profile name.
        :param language: Quality profile language.
        :param qualityProfile: Quality profile name.
        :param organization: Organization key.
        :return:
        """

    @PAGES_GET(API_QUALITYPROFILES_CHANGELOG_ENDPOINT, item="events")
    def get_history_of_changes_on_quality_profile(
        self, language, qualityProfile, organization, since=None, to=None
    ):
        """
        Get the history of changes on a quality profile: rule activation/deactivation, change in parameters/severity.
        Events are ordered by date in descending order (most recent first).

        :param language: Quality profile language.
        :param qualityProfile: Quality profile language.
        :param organization: Organization key.
        :param since: Start date for the changelog. Either a date (server timezone) or datetime can be provided.
        :param to: End date for the changelog. Either a date (server timezone) or datetime can be provided.
        :return:
        """

    @POST(API_QUALITYPROFILES_CREATE_ENDPOINT)
    def create_quality_profile(self, language, name, organization):
        """
        Create a quality profile.

        :param language: Quality profile language
        :param name: Quality profile name
        :param organization: Organization key.

        :return: request response
        """

    @POST(API_QUALITYPROFILES_DELETE_ENDPOINT)
    def delete_quality_profile(self, language, qualityProfile, organization):
        """
        Delete a quality profile and all its descendants.
        The default quality profile cannot be deleted.

        :param language: Quality profile language.
        :param qualityProfile: Quality profile name.
        :param organization: Organization key.
        :return:
        """

    @GET(API_QUALITYPROFILES_EXPORT_ENDPOINT)
    def export_quality_profile(
        self, organization, exporterKey=None, language=None, qualityProfile=None
    ):
        """
        Export a quality profile.

        :param organization: Organization key.
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

    @GET(API_QUALITYPROFILES_INHERITANCE_ENDPOINT)
    def show_quality_profile(self, language, qualityProfile, organization):
        """
        Show a quality profile's ancestors and children.

        :param language: Quality profile language.
        :param qualityProfile: Quality profile name.
        :param organization: Organization key.

        :return:
        """

    @POST(API_QUALITYPROFILES_RESTORE_ENDPOINT)
    def restore_quality_profile(self, backup, organization):
        """
        Restore a quality profile using an XML file. The restored profile name is taken from the backup file,
        so if a profile with the same name and language already exists, it will be overwritten.

        :param backup: A profile backup file in XML format, as generated by api/qualityprofiles/backup
          or the former api/profiles/backup.
        :param organization: organization key.

        :return:
        """
