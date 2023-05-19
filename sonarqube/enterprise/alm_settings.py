#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author: Jialiang Shi
from sonarqube.community.alm_settings import SonarQubeAlmSettings
from sonarqube.utils.common import GET, POST

from sonarqube.utils.config import (
    API_ALM_SETTINGS_VALIDATE_BINDING,
    API_ALM_SETTINGS_SET_GITLAB_BINDING,
    API_ALM_SETTINGS_SET_GITHUB_BINDING,
    API_ALM_SETTINGS_SET_BITBUCKET_BINDING,
    API_ALM_SETTINGS_SET_BITBUCKETCLOUD_BINDING,
    API_ALM_SETTINGS_SET_AZURE_BINDING,
    API_ALM_SETTINGS_DELETE_BINDING,
)


class SonarEnterpriseAlmSettings(SonarQubeAlmSettings):
    @POST(API_ALM_SETTINGS_SET_GITLAB_BINDING)
    def set_gitlab_binding(self, almSetting, project, repository, monorepo="false"):
        """
        since 8.1
        Bind a GitLab instance to a project.
        If the project was already bound to a previous Gitlab ALM instance,
        the binding will be updated to the new one.Requires the 'Administer' permission on the project

        :param almSetting: GitLab ALM setting key
        :param project: Project key
        :param repository: GitLab project ID
        :param monorepo: Is this project part of a monorepo (since 8.7)
        :return:
        """

    @POST(API_ALM_SETTINGS_SET_GITHUB_BINDING)
    def set_github_binding(self, almSetting, project, repository, summaryCommentEnabled="true", monorepo="false"):
        """
        since 8.1
        Bind a GitHub ALM instance to a project.
        If the project was already bound to a previous GitHub ALM instance,
        the binding will be updated to the new one.Requires the 'Administer' permission on the project

        :param almSetting: GitHub ALM setting key
        :param project: Project key
        :param repository: GitHub Repository
        :param summaryCommentEnabled: Enable/disable summary in PR discussion tab
        :param monorepo: Is this project part of a monorepo (since 8.7)
        :return:
        """

    @POST(API_ALM_SETTINGS_SET_BITBUCKET_BINDING)
    def set_bitbucket_binding(self, almSetting, project, repository, slug, monorepo="false"):
        """
        since 8.1
        Bind a Bitbucket ALM instance to a project.
        If the project was already bound to a previous Bitbucket ALM instance,
        the binding will be updated to the new one.Requires the 'Administer' permission on the project

        :param almSetting: Bitbucket ALM setting key
        :param project: Project key
        :param repository: Bitbucket repository key
        :param slug: Bitbucket repository slug
        :param monorepo: Is this project part of a monorepo (since 8.7)
        :return:
        """

    @POST(API_ALM_SETTINGS_SET_BITBUCKETCLOUD_BINDING)
    def set_bitbucketcloud_binding(self, almSetting, project, repository, monorepo="false"):
        """
        since 8.7
        Bind a Bitbucket Cloud setting to a project.
        If the project was already bound to a previous Bitbucket Cloud setting,
        the binding will be updated to the new one.Requires the 'Administer' permission on the project

        :param almSetting: Bitbucket ALM setting key
        :param project: Project key
        :param repository: Bitbucket Cloud repository key
        :param monorepo: Is this project part of a monorepo
        :return:
        """

    @POST(API_ALM_SETTINGS_SET_AZURE_BINDING)
    def set_azure_binding(self, almSetting, project, projectName, repositoryName, monorepo="false"):
        """
        since 8.1
        Bind a Azure DevOps ALM instance to a project.
        If the project was already bound to a previous Azure DevOps ALM instance,
        the binding will be updated to the new one.Requires the 'Administer' permission on the project

        :param almSetting: Azure ALM setting key
        :param project: SonarQube project key
        :param projectName: Azure project name
        :param repositoryName: Azure repository name
        :param monorepo: Is this project part of a monorepo (since 8.7)
        :return:
        """

    @POST(API_ALM_SETTINGS_DELETE_BINDING)
    def delete_binding(self, project):
        """
        since 8.1
        Delete the ALM setting binding of a project.
        Requires the 'Administer' permission on the project

        :param project: Project key
        :return:
        """

    @GET(API_ALM_SETTINGS_VALIDATE_BINDING)
    def validate_binding(self, project):
        """
        since 9.0
        Validate a project binding setting by checking connectivity and permissions
        Requires project 'Browse' permission

        :param project: Project key
        :raises ValidationError:
        :return:
        """