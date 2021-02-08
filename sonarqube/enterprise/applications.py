from sonarqube.utils.common import POST, GET
from sonarqube.utils.rest_client import RestClient

from sonarqube.utils.config import (
    API_APPLICATIONS_UPDATE_BRANCH,
    API_APPLICATIONS_UPDATE,
    API_APPLICATIONS_SHOW,
    API_APPLICATIONS_SET_TAGS,
    API_APPLICATIONS_REMOVE_PROJECT,
    API_APPLICATIONS_DELETE_BRANCH,
    API_APPLICATIONS_DELETE,
    API_APPLICATIONS_CREATE_BRANCH,
    API_APPLICATIONS_CREATE
)


class SonarApplications(RestClient):
    """
    Manage Applications
    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarApplications, self).__init__(**kwargs)

    @POST("/api/applications/add_project")
    def add_project(self, application, project):
        """
        POST api/applications/add_project
        since 7.3
        Add a project to an application.
        Requires 'Administrator' permission on the application

            Parameters

        application
        required

        Key of the application

        project
        required

        Key of the project

        Example value
        my_project
        """

    @POST(API_APPLICATIONS_CREATE)
    def create(self, name, visibility=None, description=None, key=None):
        """
        POST api/applications/create
        since 7.3
        Create a new application.
        Requires 'Administer System' permission or 'Create Applications' permission

            Parameters
            Response Example
            Changelog

        description
        optional

        Application description

        Maximum length
        256
        key
        optional

        Application key. A suitable key will be generated if not provided

        Maximum length
        400
        name
        required

        Application name

        Maximum length
        256
        visibility
        optional

        Whether the created application should be visible to everyone, or only specific user/groups.
        If no visibility is specified, the default visibility will be used.

        Possible values

            private
            public
        """

    @POST(API_APPLICATIONS_CREATE_BRANCH)
    def create_branch(self, application, branch, project, projectBranch):
        """
        POST api/applications/create_branch
        since 7.3
        Create a new branch on a given application.
        Requires 'Administrator' permission on the application

            Parameters

        application
        required

        Application key

        branch
        required

        Branch name

        Maximum length
        255
        project
        required

        Project keys. To set several values, the parameter must be called once for each value.

        Example value
        project=firstProjectKey&project=secondProjectKey&project=thirdProjectKey
        projectBranch
        required

        Project branches. To set main branch, provide an empty value. To set several values, the parameter must be
        called once for each value.

        Example value
        projectBranch=&projectBranch=branch-2.0&projectBranch=branch-2.1
        """

    @POST(API_APPLICATIONS_DELETE)
    def delete(self, application):
        """
        POST api/applications/delete
        since 7.3
        Delete an application definition.
        Requires 'Administrator' permission on the application

            Parameters

        application
        required

        Application key
        """

    @POST(API_APPLICATIONS_DELETE_BRANCH)
    def delete_branch(self, application, branch):
        """
        POST api/applications/delete_branch
        since 7.3
        Delete a branch on a given application.
        Requires 'Administrator' permission on the application

            Parameters

        application
        required

        Application key

        branch
        required

        Branch name
        """

    @POST(API_APPLICATIONS_REMOVE_PROJECT)
    def remove_project(self, application, project):
        """
        POST api/applications/remove_project
        since 7.3
        Add a project to an application
        Requires 'Administrator' permission on the application

            Parameters

        application
        required

        Key of the application

        project
        required

        Key of the project

        Example value
        my_project
        """

    @POST(API_APPLICATIONS_SET_TAGS)
    def set_tags(self, application, tags):
        """
        POST api/applications/set_tags
        since 8.3
        Set tags on a application.
        Requires the following permission: 'Administer' rights on the specified application

            Parameters

        application
        required

        Application key

        tags
        required

        Comma-separated list of tags

        Example value
        finance, offshore
        """

    @GET(API_APPLICATIONS_SHOW)
    def show(self, application, branch):
        """
        GET api/applications/show
        since 7.3
        Returns an application and its associated projects.
        Requires the 'Browse' permission on the application.

            Parameters
            Response Example
            Changelog

        application
        required

        Application key

        Example value
        my_application
        branch
        optional

        Branch name

        Example value
        branch-2.0
        """

    @POST(API_APPLICATIONS_UPDATE)
    def update(self, application, name, description=None):
        """
        POST api/applications/update
        since 7.3
        Update an application.
        Requires 'Administrator' permission on the application

            Parameters

        application
        required

        Application key

        description
        optional

        New description for the application

        Maximum length
        256
        name
        required

        New name for the application

        Maximum length
        256
        """

    @POST(API_APPLICATIONS_UPDATE_BRANCH)
    def update_branch(self, application, branch, name, project, projectBranch):
        """
        POST api/applications/update_branch
        since 7.3
        Update a branch on a given application.
        Requires 'Administrator' permission on the application

            Parameters

        application
        required

        Application key

        Example value
        my_application
        branch
        required

        Branch name

        Example value
        branch-2.0
        name
        required

        New branch name

        Maximum length
        255
        project
        required

        Project keys. To set several values, the parameter must be called once for each value.

        Example value
        project=firstProjectKey&project=secondProjectKey&project=thirdProjectKey
        projectBranch
        required

        Project branches. To set main branch, provide an empty value. To set several values, the parameter must be
        called once for each value.

        Example value
        projectBranch=&projectBranch=branch-2.0&projectBranch=branch-2.1
        """