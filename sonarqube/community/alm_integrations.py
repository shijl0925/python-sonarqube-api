from sonarqube.utils.common import POST, GET
from sonarqube.utils.rest_client import RestClient

from sonarqube.utils.config import (
    API_ALM_INTEGRATION_SET_PAT,
    API_ALM_INTEGRATION_SEARCH_GITLAB_REPOS,
    API_ALM_INTEGRATION_SEARCH_BITBUCKETSERVER_REPOS,
    API_ALM_INTEGRATION_SEARCH_BITBUCKETCLOUD_REPOS,
    API_ALM_INTEGRATION_SEARCH_AZURE_REPOS,
    API_ALM_INTEGRATION_LIST_BITBUCKETSERVER_PROJECTS,
    API_ALM_INTEGRATION_LIST_AZURE_PROJECTS,
    API_ALM_INTEGRATION_IMPORT_GITLAB_PROJECT
)


class SonarQubeAlmIntegrations(RestClient):

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeAlmIntegrations, self).__init__(**kwargs)

    @POST(API_ALM_INTEGRATION_IMPORT_GITLAB_PROJECT)
    def import_gitlab_project(self, almSetting, gitlabProjectId):
        """
        since 8.5
        Import a GitLab project to SonarQube, creating a new project and configuring MR decoration
        Requires the 'Create Projects' permission

        :param almSetting: ALM setting key
        :param gitlabProjectId: GitLab project ID
        :return:
        """

    @GET(API_ALM_INTEGRATION_LIST_AZURE_PROJECTS)
    def list_azure_projects(self, almSetting):
        """
        since 8.6
        List Azure projects
        Requires the 'Create Projects' permission

        :param almSetting: ALM setting key
        :return:
        """

    @GET(API_ALM_INTEGRATION_LIST_BITBUCKETSERVER_PROJECTS)
    def list_bitbucketserver_projects(self, almSetting):
        """
        since 8.2
        List the Bitbucket Server projects
        Requires the 'Create Projects' permission

        :param almSetting: ALM setting key
        :return:
        """

    @GET(API_ALM_INTEGRATION_SEARCH_AZURE_REPOS)
    def search_azure_repos(self, almSetting, projectName=None, searchQuery=None):
        """
        since 8.6
        Search the Azure repositories
        Requires the 'Create Projects' permission

        :param almSetting: ALM setting key
        :param projectName: Project name filter
        :param searchQuery: Search query filter
        :return:
        """

    @GET(API_ALM_INTEGRATION_SEARCH_BITBUCKETSERVER_REPOS)
    def search_bitbucketserver_repos(self, almSetting, projectName=None, repositoryName=None):
        """
        since 8.2
        Search the Bitbucket Server repositories with REPO_ADMIN access
        Requires the 'Create Projects' permission

        :param almSetting: ALM setting key
        :param projectName: Project name filter
        :param repositoryName: Repository name filter
        :return:
        """

    @GET(API_ALM_INTEGRATION_SEARCH_BITBUCKETCLOUD_REPOS)
    def search_bitbucketserver_repos(self, almSetting, repositoryName=None):
        """
        since 9.0
        Search the Bitbucket Cloud repositories
        Requires the 'Create Projects' permission

        :param almSetting: ALM setting key
        :param repositoryName: Repository name filter
        :return:
        """

    @GET(API_ALM_INTEGRATION_SEARCH_GITLAB_REPOS)
    def search_gitlab_repos(self, almSetting, p=None, projectName=None, ps=None):
        """
        since 8.5
        Search the GitLab projects.
        Requires the 'Create Projects' permission

        :param almSetting: ALM setting key
        :param p: 1-based page number
        :param projectName: Project name filter
        :param ps: Page size. Must be greater than 0 and less or equal than 500
        :return:
        """

    @POST(API_ALM_INTEGRATION_SET_PAT)
    def set_pat(self, almSetting, pat, username=None):
        """
        since 8.2
        Set a Personal Access Token for the given ALM setting
        Only valid for Azure DevOps, Bitbucket Server & GitLab Alm Setting
        Requires the 'Create Projects' permission

        :param almSetting: ALM setting key
        :param pat: Personal Access Token
        :param username: Username
        :return:
        """