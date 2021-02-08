from sonarqube.utils.common import GET, POST
from sonarqube.utils.rest_client import RestClient

from sonarqube.utils.config import (
    API_ALM_SETTINGS_VALIDATE,
    API_ALM_SETTINGS_UPDATE_GITLAB,
    API_ALM_SETTINGS_UPDATE_GITHUB,
    API_ALM_SETTINGS_UPDATE_BITBUCKET,
    API_ALM_SETTINGS_UPDATE_AZURE,
    API_ALM_SETTINGS_SET_GITLAB_BINDING,
    API_ALM_SETTINGS_SET_GITHUB_BINDING,
    API_ALM_SETTINGS_SET_BITBUCKET_BINDING,
    API_ALM_SETTINGS_SET_AZURE_BINDING,
    API_ALM_SETTINGS_LIST_DEFINITIONS,
    API_ALM_SETTINGS_LIST,
    API_ALM_SETTINGS_DELETE_BINDING,
    API_ALM_SETTINGS_CREATE_GITLAB,
    API_ALM_SETTINGS_CREATE_GITHUB,
    API_ALM_SETTINGS_CREATE_BITBUCKET,
    API_ALM_SETTINGS_CREATE_AZURE,
    API_ALM_SETTINGS_COUNT_BINDING
)


class SonarAlmSettings(RestClient):

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarAlmSettings, self).__init__(**kwargs)

    def get(self, key):
        result = self.list()
        for alm_setting in result["almSettings"]:
            if alm_setting["key"] == key:
                return alm_setting

    @GET(API_ALM_SETTINGS_COUNT_BINDING)
    def count_binding(self, almSetting):
        """
        GET api/alm_settings/count_binding
        since 8.1
        Count number of project bound to an ALM setting.
        Requires the 'Administer System' permission

            Parameters
            Response Example

        almSetting
        required

        ALM setting key
        """

    @POST(API_ALM_SETTINGS_CREATE_AZURE)
    def create_azure(self, key, personalAccessToken, url):
        """
        POST api/alm_settings/create_azure
        since 8.1
        Create Azure ALM instance Setting.
        Requires the 'Administer System' permission

            Parameters
            Changelog

        key
        required

        Unique key of the Azure Devops instance setting

        Maximum length
        200
        personalAccessToken
        required

        Azure Devops personal access token

        Maximum length
        2000
        url
        required

        Azure API URL

        Maximum length
        2000
        """

    @POST(API_ALM_SETTINGS_CREATE_BITBUCKET)
    def create_bitbucket(self, key, personalAccessToken, url):
        """
        POST api/alm_settings/create_bitbucket
        since 8.1
        Create Bitbucket ALM instance Setting.
        Requires the 'Administer System' permission
        
            Parameters
        
        key
        required
            
        Unique key of the Bitbucket instance setting
            
        Maximum length
        200
        personalAccessToken
        required
            
        Bitbucket personal access token
            
        Maximum length
        2000
        url
        required
            
        BitBucket server API URL
            
        Maximum length
        2000
        """

    @POST(API_ALM_SETTINGS_CREATE_GITHUB)
    def create_github(self, appId, clientId, clientSecret, key, privateKey, url):
        """
        POST api/alm_settings/create_github
        since 8.1
        Create GitHub ALM instance Setting.
        Requires the 'Administer System' permission
        
            Parameters
        
        appId
        required
            
        GitHub App ID
            
        Maximum length
        80
        clientId
        required
            
        GitHub App Client ID
            
        Maximum length
        80
        clientSecret
        required
            
        GitHub App Client Secret
            
        Maximum length
        80
        key
        required
            
        Unique key of the GitHub instance setting
            
        Maximum length
        200
        privateKey
        required
            
        GitHub App private key
            
        Maximum length
        2000
        url
        required
            
        GitHub API URL
            
        Maximum length
        2000
        """

    @POST(API_ALM_SETTINGS_CREATE_GITLAB)
    def create_gitlab(self, key, personalAccessToken, url):
        """
        POST api/alm_settings/create_gitlab
        since 8.1
        Create GitLab ALM instance Setting.
        Requires the 'Administer System' permission
        
            Parameters
            Changelog
        
        key
        required
            
        Unique key of the GitLab instance setting
            
        Maximum length
        200
        personalAccessToken
        required
            
        GitLab personal access token
            
        Maximum length
        2000
        url
        required
            
        GitLab API URL
            
        Maximum length
        2000
        POST api/alm_settings/delete
        since 8.1
        Delete an ALM Settings.
        Requires the 'Administer System' permission
        
            Parameters
        
        key
        required
            
        ALM Setting key
            
        """

    @POST(API_ALM_SETTINGS_DELETE_BINDING)
    def delete_binding(self, key):
        """
        POST api/alm_settings/delete_binding
        since 8.1
        Delete the ALM setting binding of a project.
        Requires the 'Administer' permission on the project
        
            Parameters
        
        project
        required
            
        Project key
            
        GET api/alm_settings/get_binding
        since 8.1
        Get ALM binding of a given project.
        Requires the 'Administer' permission on the project
        
            Parameters
            Response Example
            Changelog
        
        project
        required
            
        Project key
        
        """

    @GET(API_ALM_SETTINGS_LIST)
    def list(self, project=None):
        """	
        GET api/alm_settings/list
        since 8.1
        List ALM setting available for a given project, sorted by ALM key
        Requires the 'Administer project' permission if the 'project' parameter is provided, requires the 'Create Projects' permission otherwise.
        
            Parameters
            Response Example
            Changelog
        
        project
        optional
            
        Project key
        """

    @GET(API_ALM_SETTINGS_LIST_DEFINITIONS)
    def list_definitions(self):
        """	
        GET api/alm_settings/list_definitions
        since 8.1
        List ALM Settings, sorted by created date.
        Requires the 'Administer System' permission
        
            Response Example
            Changelog
        
        {
          "github": [
            {
              "key": "GitHub Server - Dev Team",
              "url": "https://github.enterprise.com",
              "appId": "12345",
              "privateKey": "54684654",
              "clientId": "client_id",
              "clientSecret": "client_secret"
            }
          ],
          "azure": [
            {
              "key": "Azure Devops Server - Dev Team",
              "personalAccessToken": "12345"
            }
          ],
          "bitbucket": [
            {
              "key": "Bitbucket Server - Dev Team",
              "url": "https://bitbucket.enterprise.com",
              "personalAccessToken": "abcdef"
            }
          ],
          "gitlab": [
            {
              "key": "Gitlab - Dev Team",
              "personalAccessToken": "12345"
            }
          ]
        }
        """

    @POST(API_ALM_SETTINGS_SET_AZURE_BINDING)
    def set_azure_binding(self, almSetting, project, projectName, repositoryName ):
        """
        POST api/alm_settings/set_azure_binding
        since 8.1
        Bind a Azure DevOps ALM instance to a project.
        If the project was already bound to a previous Azure DevOps ALM instance, the binding will be updated to the new one.Requires the 'Administer' permission on the project
        
            Parameters
        
        almSetting
        required
            
        Azure ALM setting key
            
        project
        required
            
        SonarQube project key
            
        projectName
        required
        since 8.6
            
        Azure project name
            
        repositoryName
        required
        since 8.6
            
        Azure repository name
        """

    @POST(API_ALM_SETTINGS_SET_BITBUCKET_BINDING)
    def set_bitbucket_binding(self, almSetting, project, repository, slug):
        """	
        POST api/alm_settings/set_bitbucket_binding
        since 8.1
        Bind a Bitbucket ALM instance to a project.
        If the project was already bound to a previous Bitbucket ALM instance, the binding will be updated to the new one.Requires the 'Administer' permission on the project
        
            Parameters
        
        almSetting
        required
            
        GitHub ALM setting key
            
        project
        required
            
        Project key
            
        repository
        required
            
        Bitbucket repository key
            
        slug
        required
            
        Bitbucket repository slug
        """

    @POST(API_ALM_SETTINGS_SET_GITHUB_BINDING)
    def set_github_binding(self, almSetting, project, repository, summaryContentEnabled=True):
        """	
        POST api/alm_settings/set_github_binding
        since 8.1
        Bind a GitHub ALM instance to a project.
        If the project was already bound to a previous GitHub ALM instance, the binding will be updated to the new one.Requires the 'Administer' permission on the project
        
            Parameters
            Changelog
        
        almSetting
        required
            
        GitHub ALM setting key
            
        project
        required
            
        Project key
            
        repository
        required
            
        GitHub Repository
            
        Maximum length
        256
        summaryCommentEnabled
        optional
            
        Enable/disable summary in PR discussion tab
            
        Default value
        true
        """

    @POST(API_ALM_SETTINGS_SET_GITLAB_BINDING)
    def set_gitlab_binding(self, almSetting, project, repository):

        """
        POST api/alm_settings/set_gitlab_binding
        since 8.1
        Bind a GitLab instance to a project.
        If the project was already bound to a previous Gitlab ALM instance, the binding will be updated to the new one.Requires the 'Administer' permission on the project
        
            Parameters
            almSetting
            required

            GitLab ALM setting key

            project
            required

            Project key

            repository
            required

            GitLab project ID
            Changelog
        """

    @POST(API_ALM_SETTINGS_UPDATE_AZURE)
    def update_azure(self, key, personalAccessToken, url, newKey=None):
        """
        POST api/alm_settings/update_azure
        since 8.1
        Update Azure ALM instance Setting.
        Requires the 'Administer System' permission
        
            Parameters
            Changelog
        
        key
        required
            
        Unique key of the Azure instance setting
            
        Maximum length
        200
        newKey
        optional
            
        Optional new value for an unique key of the Azure Devops instance setting
            
        Maximum length
        200
        personalAccessToken
        required
            
        Azure Devops personal access token
            
        Maximum length
        2000
        url
        required
            
        Azure API URL
            
        Maximum length
        2000
        """

    @POST(API_ALM_SETTINGS_UPDATE_BITBUCKET)
    def update_bitbucket(self, key, personalAccessToken, url, newKey=None):
        """
        POST api/alm_settings/update_bitbucket
        since 8.1
        Update Bitbucket ALM instance Setting.
        Requires the 'Administer System' permission
        
            Parameters
        
        key
        required
            
        Unique key of the Bitbucket instance setting
            
        Maximum length
        200
        newKey
        optional
            
        Optional new value for an unique key of the Bitbucket instance setting
            
        Maximum length
        200
        personalAccessToken
        required
            
        Bitbucket personal access token
            
        Maximum length
        2000
        url
        required
            
        Bitbucket API URL
            
        Maximum length
        2000
        """

    @POST(API_ALM_SETTINGS_UPDATE_GITHUB)
    def update_github(self, appId, clientId, clientSecret, key, privateKey, url, newKey=None):
        """
        POST api/alm_settings/update_github
        since 8.1
        Update GitHub ALM instance Setting.
        Requires the 'Administer System' permission
        
            Parameters
        
        appId
        required
            
        GitHub API ID
            
        Maximum length
        80
        clientId
        required
            
        GitHub App Client ID
            
        Maximum length
        80
        clientSecret
        required
            
        GitHub App Client Secret
            
        Maximum length
        80
        key
        required
            
        Unique key of the GitHub instance setting
            
        Maximum length
        200
        newKey
        optional
            
        Optional new value for an unique key of the GitHub instance setting
            
        Maximum length
        200
        privateKey
        required
            
        GitHub App private key
            
        Maximum length
        2000
        url
        required
            
        GitHub API URL
            
        Maximum length
        2000
        """

    @POST(API_ALM_SETTINGS_UPDATE_GITLAB)
    def update_gitlab(self, key, personalAccessToken, url, newKey=None):
        """
        POST api/alm_settings/update_gitlab
        since 8.1
        Update GitLab ALM instance Setting.
        Requires the 'Administer System' permission
        
            Parameters
            Changelog
        
        key
        required
            
        Unique key of the GitLab instance setting
            
        Maximum length
        200
        newKey
        optional
            
        Optional new value for an unique key of the GitLab instance setting
            
        Maximum length
        200
        personalAccessToken
        required
            
        GitLab personal access token
            
        Maximum length
        2000
        url
        required
            
        GitLab API URL
            
        Maximum length
        2000
        
        """

    @GET(API_ALM_SETTINGS_VALIDATE)
    def validate(self, key):
        """
        GET api/alm_settings/validate
        since 8.6
        Validate an ALM Setting by checking connectivity and permissions
        Requires the 'Administer System' permission
        
            Parameters
        
        key
        required
            
        Unique key of the ALM settings
            
        Maximum length
        200
        """