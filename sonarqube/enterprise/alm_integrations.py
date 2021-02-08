from sonarqube.utils.common import POST, GET
from sonarqube.utils.rest_client import RestClient

from sonarqube.utils.config import (
    API_ALM_INTEGRATION_SET_PAT,
    API_ALM_INTEGRATION_SEARCH_GITLAB_REPOS,
    API_ALM_INTEGRATION_SEARCH_BITBUCKETSERVER_REPOS,
    API_ALM_INTEGRATION_SEARCH_AZURE_REPOS,
    API_ALM_INTEGRATION_SEARCH_BITBUCKETSERVER_PROJECTS,
    API_ALM_INTEGRATION_LIST_AZURE_PROJECTS,
    API_ALM_INTEGRATION_IMPORT_GITLAB_PROJECT
)


class SonarAlmIntegrations(RestClient):

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarAlmIntegrations, self).__init__(**kwargs)

    @POST(API_ALM_INTEGRATION_IMPORT_GITLAB_PROJECT)
    def import_gitlab_project(self, almSettings, gitlabProjectId):
        """
        api/alm_integrations
        Manage ALM Integrations
        POST api/alm_integrations/import_gitlab_project
        since 8.5
        Import a GitLab project to SonarQube, creating a new project and configuring MR decoration
        Requires the 'Create Projects' permission

            Parameters
        """

    @GET(API_ALM_INTEGRATION_LIST_AZURE_PROJECTS)
    def list_azure_projects(self, almSetting):
        """

        GET api/alm_integrations/list_azure_projects
        since 8.6
        List Azure projects
        Requires the 'Create Projects' permission

            Parameters

        """

    @GET(API_ALM_INTEGRATION_SEARCH_BITBUCKETSERVER_PROJECTS)
    def list_bitbucketserver_projects(self, almSettings):
        """

        GET api/alm_integrations/list_bitbucketserver_projects
        since 8.2
        List the Bitbucket Server projects
        Requires the 'Create Projects' permission

            Parameters
        """

    @GET(API_ALM_INTEGRATION_SEARCH_AZURE_REPOS)
    def search_azure_repos(self, almSetting, projectName=None, searchQuery=None):
        """

        GET api/alm_integrations/search_azure_repos
        since 8.6
        Search the Azure repositories
        Requires the 'Create Projects' permission

            Parameters
        """

    @GET(API_ALM_INTEGRATION_SEARCH_BITBUCKETSERVER_REPOS)
    def search_bitbucketserver_repos(self, almSetting, projectName=None, repositoryName=None):
        """

        GET api/alm_integrations/search_bitbucketserver_repos
        since 8.2
        Search the Bitbucket Server repositories with REPO_ADMIN access
        Requires the 'Create Projects' permission

            Parameters
        """

    @GET(API_ALM_INTEGRATION_SEARCH_GITLAB_REPOS)
    def search_gitlab_repos(self, almSettings, p=None, projectName=None, ps=None):
        """

        GET api/alm_integrations/search_gitlab_repos
        since 8.5
        Search the GitLab projects.
        Requires the 'Create Projects' permission

            Parameters
            Response Example
        """

    @POST(API_ALM_INTEGRATION_SET_PAT)
    def set_pat(self, almSetting, pat):
        """

        POST api/alm_integrations/set_pat
        since 8.2
        Set a Personal Access Token for the given ALM setting
        Only valid for Azure DevOps, Bitbucket Server & GitLab Alm Setting
        Requires the 'Create Projects' permission

            Parameters
        """