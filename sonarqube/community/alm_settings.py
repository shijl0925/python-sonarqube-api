from sonarqube.utils.common import GET, POST
from sonarqube.utils.rest_client import RestClient

from sonarqube.utils.config import (
    API_ALM_SETTINGS_VALIDATE,
    API_ALM_SETTINGS_UPDATE_GITLAB,
    API_ALM_SETTINGS_UPDATE_GITHUB,
    API_ALM_SETTINGS_UPDATE_BITBUCKET,
    API_ALM_SETTINGS_UPDATE_BITBUCKETCLOUD,
    API_ALM_SETTINGS_UPDATE_AZURE,
    API_ALM_SETTINGS_SET_GITLAB_BINDING,
    API_ALM_SETTINGS_SET_GITHUB_BINDING,
    API_ALM_SETTINGS_SET_BITBUCKET_BINDING,
    API_ALM_SETTINGS_SET_BITBUCKETCLOUD_BINDING,
    API_ALM_SETTINGS_SET_AZURE_BINDING,
    API_ALM_SETTINGS_LIST_DEFINITIONS,
    API_ALM_SETTINGS_LIST,
    API_ALM_SETTINGS_DELETE,
    API_ALM_SETTINGS_GET_BINDING,
    API_ALM_SETTINGS_DELETE_BINDING,
    API_ALM_SETTINGS_CREATE_GITLAB,
    API_ALM_SETTINGS_CREATE_GITHUB,
    API_ALM_SETTINGS_CREATE_BITBUCKET,
    API_ALM_SETTINGS_CREATE_BITBUCKETCLOUD,
    API_ALM_SETTINGS_CREATE_AZURE,
    API_ALM_SETTINGS_COUNT_BINDING
)


class SonarQubeAlmSettings(RestClient):

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeAlmSettings, self).__init__(**kwargs)

    def get(self, key):
        result = self.list()
        for alm_setting in result["almSettings"]:
            if alm_setting["key"] == key:
                return alm_setting

    @GET(API_ALM_SETTINGS_COUNT_BINDING)
    def count_binding(self, almSetting):
        """
        since 8.1
        Count number of project bound to an ALM setting.
        Requires the 'Administer System' permission

        :param almSetting: ALM setting key
        :return:
        """

    @POST(API_ALM_SETTINGS_CREATE_AZURE)
    def create_azure(self, key, personalAccessToken, url):
        """
        since 8.1
        Create Azure ALM instance Setting.
        Requires the 'Administer System' permission

        :param key: Unique key of the Azure Devops instance setting
        :param personalAccessToken: Azure Devops personal access token
        :param url: Azure API URL
        :return:
        """

    @POST(API_ALM_SETTINGS_CREATE_BITBUCKET)
    def create_bitbucket(self, key, personalAccessToken, url):
        """
        since 8.1
        Create Bitbucket ALM instance Setting.
        Requires the 'Administer System' permission

        :param key: Unique key of the Bitbucket instance setting
        :param personalAccessToken: Bitbucket personal access token
        :param url: BitBucket server API URL
        :return:
        """

    @POST(API_ALM_SETTINGS_CREATE_BITBUCKETCLOUD)
    def create_bitbucket(self, clientId, clientSecret, key, workspace):
        """
        since 8.7
        Configure a new instance of Bitbucket Cloud.
        Requires the 'Administer System' permission

        :param clientId: Bitbucket Cloud Client ID
        :param clientSecret: Bitbucket Cloud Client Secret
        :param key: Unique key of the Bitbucket Cloud setting
        :param workspace: Bitbucket Cloud workspace ID
        :return:
        """

    @POST(API_ALM_SETTINGS_CREATE_GITHUB)
    def create_github(self, appId, clientId, clientSecret, key, privateKey, url):
        """
        since 8.1
        Create GitHub ALM instance Setting.
        Requires the 'Administer System' permission

        :param appId: GitHub App ID
        :param clientId: GitHub App Client ID
        :param clientSecret: GitHub App Client Secret
        :param key: Unique key of the GitHub instance setting
        :param privateKey: GitHub App private key
        :param url: GitHub API URL
        :return:
        """

    @POST(API_ALM_SETTINGS_CREATE_GITLAB)
    def create_gitlab(self, key, personalAccessToken, url):
        """
        since 8.1
        Create GitLab ALM instance Setting.
        Requires the 'Administer System' permission

        :param key: Unique key of the GitLab instance setting
        :param personalAccessToken: GitLab personal access token
        :param url: GitLab API URL
        :return:
        """

    @POST(API_ALM_SETTINGS_DELETE)
    def delete(self, key):
        """
        since 8.1
        Delete an ALM Settings.
        Requires the 'Administer System' permission

        :param key: ALM Setting key
        :return:
        """

    @GET(API_ALM_SETTINGS_GET_BINDING)
    def get_binding(self, project):
        """
        SINCE 8.1
        Get ALM binding of a given project.
        Requires the 'Administer' permission on the project

        :param project: Project key
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

    @GET(API_ALM_SETTINGS_LIST)
    def list(self, project=None):
        """
        since 8.1
        List ALM setting available for a given project, sorted by ALM key
        Requires the 'Administer project' permission if the 'project' parameter is provided,
        requires the 'Create Projects' permission otherwise.

        :param project: Project key
        :return:
        """

    @GET(API_ALM_SETTINGS_LIST_DEFINITIONS)
    def list_definitions(self):
        """
        since 8.1
        List ALM Settings, sorted by created date.
        Requires the 'Administer System' permission

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

    @POST(API_ALM_SETTINGS_UPDATE_AZURE)
    def update_azure(self, key, personalAccessToken, url, newKey=None):
        """
        since 8.1
        Update Azure ALM instance Setting.
        Requires the 'Administer System' permission

        :param key: Unique key of the Azure instance setting
        :param personalAccessToken: Azure Devops personal access token
        :param url: Azure API URL
        :param newKey: Optional new value for an unique key of the Azure Devops instance setting
        :return:
        """

    @POST(API_ALM_SETTINGS_UPDATE_BITBUCKET)
    def update_bitbucket(self, key, personalAccessToken, url, newKey=None):
        """
        since 8.1
        Update Bitbucket ALM instance Setting.
        Requires the 'Administer System' permission

        :param key: Unique key of the Bitbucket instance setting
        :param personalAccessToken: Bitbucket personal access token
        :param url: Bitbucket API URL
        :param newKey: Optional new value for an unique key of the Bitbucket instance setting
        :return:
        """

    @POST(API_ALM_SETTINGS_UPDATE_BITBUCKETCLOUD)
    def update_bitbucket(self, key, personalAccessToken, url, workspace, newKey=None):
        """
        since 8.7
        Update Bitbucket ALM instance Setting.
        Requires the 'Administer System' permission

        :param key: Unique key of the Bitbucket instance setting
        :param personalAccessToken: Bitbucket personal access token
        :param url: Bitbucket API URL
        :param workspace: Bitbucket Cloud workspace ID
        :param newKey: Optional new value for an unique key of the Bitbucket instance setting
        :return:
        """

    @POST(API_ALM_SETTINGS_UPDATE_GITHUB)
    def update_github(self, appId, clientId, clientSecret, key, privateKey, url, newKey=None):
        """
        since 8.1
        Update GitHub ALM instance Setting.
        Requires the 'Administer System' permission

        :param appId: GitHub API ID
        :param clientId: GitHub App Client ID
        :param clientSecret: GitHub App Client Secret
        :param key: Unique key of the GitHub instance setting
        :param privateKey: GitHub App private key
        :param url: GitHub API URL
        :param newKey: Optional new value for an unique key of the GitHub instance setting
        :return:
        """

    @POST(API_ALM_SETTINGS_UPDATE_GITLAB)
    def update_gitlab(self, key, personalAccessToken, url, newKey=None):
        """
        since 8.1
        Update GitLab ALM instance Setting.
        Requires the 'Administer System' permission

        :param key: Unique key of the GitLab instance setting
        :param personalAccessToken: GitLab personal access token
        :param url: GitLab API URL
        :param newKey: Optional new value for an unique key of the GitLab instance setting
        :return:
        """

    @GET(API_ALM_SETTINGS_VALIDATE)
    def validate(self, key):
        """
        since 8.6
        Validate an ALM Setting by checking connectivity and permissions
        Requires the 'Administer System' permission

        :param key: Unique key of the ALM settings
        :return:
        """
