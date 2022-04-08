from sonarqube.utils.common import POST, GET
from sonarqube.utils.rest_client import RestClient

from sonarqube.utils.config import (
    API_VIEWS_UPDATE,
    API_VIEWS_SHOW,
    API_VIEWS_SET_TAGS_MODE,
    API_VIEWS_SET_REMAINING_PROJECTS_MODE,
    API_VIEWS_SET_REGEXP_MODE,
    API_VIEWS_SET_MANUAL_MODE,
    API_VIEWS_REMOVE_PROJECT,
    API_VIEWS_MOVE_OPTIONS,
    API_VIEWS_MOVE,
    API_VIEWS_LOCAL_VIEWS,
    API_VIEWS_LIST,
    API_VIEWS_DEFINITION,
    API_VIEWS_DEFINE,
    API_VIEWS_CREATE,
    API_VIEWS_DELETE,
    API_VIEWS_ADD_SUB_VIEW,
    API_VIEWS_ADD_PROJECT,
    API_VIEWS_ADD_LOCAL_VIEW,
    API_VIEWS_SET_NONE_MODE_VIEW,
    API_VIEWS_ADD_PROJECT_BRANCH_VIEW,
    API_VIEWS_REMOVE_PROJECT_BRANCH_VIEW,
    API_VIEWS_ADD_APPLICATION_BRANCH_VIEW,
    API_VIEWS_REMOVE_APPLICATION_BRANCH_VIEW,
    API_VIEWS_APPLICATIONS_VIEW,
    API_VIEWS_ADD_APPLICATION_VIEW,
    API_VIEWS_REMOVE_APPLICATION_VIEW,
    API_VIEWS_PORTFOLIOS_VIEW,
    API_VIEWS_ADD_PORTFOLIO_VIEW,
    API_VIEWS_REMOVE_PORTFOLIO_VIEW
)


class SonarQubeViews(RestClient):
    """
    Manage Portfolios
    """

    special_attributes_map = {"definition": "def"}

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(SonarQubeViews, self).__init__(**kwargs)

    def get(self, key):
        result = self.list()
        for view in result["views"]:
            if view["key"] == key:
                return view

    @POST(API_VIEWS_ADD_LOCAL_VIEW)
    def add_local_view(self, key, ref_key):
        """
        since 1.0
        Add a local reference to an existing portfolio
        Authentication is required for this API endpoint

        :param key: Key of the parent portfolio
        :param ref_key: Key of the referenced local portfolio
        :return:
        """

    @POST(API_VIEWS_ADD_PROJECT)
    def add_project(self, key, project):
        """
        since 1.0
        Add a project to a portfolio
        Requires 'Administrator' permission on the portfolio and 'Browse' permission for adding project

        :param key: Key of the portfolio
        :param project: Key of the project
        :return:
        """

    @POST(API_VIEWS_ADD_SUB_VIEW)
    def add_sub_view(self, key, name, description=None, subKey=None):
        """
        since 1.0
        Add a portfolio to an existing portfolio
        Authentication is required for this API endpoint

        :param key: Key of the parent portfolio
        :param name: Name of the new portfolio
        :param description: Description of the new portfolio, can be left blank
        :param subKey: If specified, will be used for the new portfolio's key instead of the default generated value
        :return:
        """

    @POST(API_VIEWS_CREATE)
    def create(self, name, description=None, key=None, visibility=None):
        """
        since 1.0
        Create a new (root) portfolio.
        Requires 'Administer System' permission or 'Create Portfolios' permission

        :param name: Name for the new portfolio
        :param description: Description for the new portfolio, can be left blank
        :param key: Key for the new portfolio. A suitable key will be generated if not provided
        :param visibility: Whether the created portfolio or application should be visible to everyone,
          or only specific user/groups.
          If no visibility is specified, the default visibility of the organization will be used.
          Possible values: private, public

        :return:
        """

    @POST(API_VIEWS_DEFINE)
    def define(self, definition):
        """
        since 1.0
        Define the portfolio structure by uploading a XML definition file. The uploaded file is validated against the
        XML Schema available on the server and its structure is checked for inconsistencies (e.g loops in local
        references, duplicate project associations). If the file is deemed valid, the portfolio hierarchy is updated
        according to the contents of the file. Requires Provision Projects permission.

        :param definition: XML file to upload and validate
        :return:
        """

    @GET(API_VIEWS_DEFINITION)
    def definition(self):
        """
        since 2.0
        Return the definition of the structure of portfolios in XML format.
        Requires Create Projects permission.

        :return:
        """

    @POST(API_VIEWS_DELETE)
    def delete(self, key):
        """
        since 1.0
        Delete a portfolio definition.
        Requires 'Administrator' permission on the portfolio

        :param key: Portfolio key
        :return:
        """

    @GET(API_VIEWS_LIST)
    def list(self):
        """
        since 1.0
        List root portfolios.
        Requires authentication. Only portfolios with the admin permission are returned.

        :return:
        """

    @GET(API_VIEWS_LOCAL_VIEWS)
    def local_views(self, key):
        """
        since 1.0
        List portfolios that can be locally referrenced
        Authentication is required for this API endpoint

        :param key: Key of the would-be parent portfolio
        :return:
        """

    @POST(API_VIEWS_MOVE)
    def move(self, destination, key):
        """
        since 1.0
        Move a portfolio
        Authentication is required for this API endpoint

        :param destination: Key of the destination portfolio
        :param key: Key of the portfolio to move
        :return:
        """

    @GET(API_VIEWS_MOVE_OPTIONS)
    def move_options(self, key):
        """
        since 1.0
        List possible portfolio destinations
        Authentication is required for this API endpoint

        :param key: Key of the portfolio to move
        :return:
        """

    @POST(API_VIEWS_REMOVE_PROJECT)
    def remove_project(self, key, project):
        """
        since 1.0
        Remove a project from a portfolio
        Requires 'Administrator' permission on the portfolio

        :param key: Key of the portfolio
        :param project: Key of the project
        :return:
        """

    @POST(API_VIEWS_SET_MANUAL_MODE)
    def set_manual_mode(self, portfolio):
        """
        since 7.4
        Set the projects selection mode of a portfolio on manual selection.
        In order to add project, please use api/view/add_project.
        Requires 'Administrator' permission on the portfolio

        :param portfolio: Key of the portfolio or sub-portfolio to update
        :return:
        """

    @POST(API_VIEWS_SET_REGEXP_MODE)
    def set_regexp_mode(self, portfolio, regexp):
        """
        since 7.4
        Set the projects selection mode of a portfolio on regular expression.
        Requires 'Administrator' permission on the portfolio

        :param portfolio: Key of the portfolio or sub-portfolio to update
        :param regexp: A valid regexp with respect to the JDK's ``java.util.regex.Pattern`` class
        :return:
        """

    @POST(API_VIEWS_SET_REMAINING_PROJECTS_MODE)
    def set_remaining_projects_mode(self, portfolio):
        """
        since 7.4
        Set the projects selection mode of a portfolio on unassociated projects in hierarchy.
        Requires 'Administrator' permission on the portfolio

        :param portfolio: Key of the portfolio or sub-portfolio to update
        :return:
        """

    @POST(API_VIEWS_SET_TAGS_MODE)
    def set_tags_mode(self, portfolio, tags):
        """
        since 7.4
        Set the projects selection mode of a portfolio on project tags.
        Requires 'Administrator' permission on the portfolio

        :param portfolio: Key of the portfolio or sub-portfolio to update
        :param tags: Comma-separated list of tags. It's not possible to set nothing.
        :return:
        """

    @GET(API_VIEWS_SHOW)
    def show(self, key):
        """
        since 1.0
        Show the details of a portfolio, including its hierarchy and project selection mode.
        Authentication is required for this API endpoint

        :param key: The key of the portfolio
        :return:
        """

    @POST(API_VIEWS_UPDATE)
    def update(self, key, name, description=None):
        """
        since 1.0
        Update a portfolio.
        Requires 'Administrator' permission on the portfolio

        :param key: Key of the portfolio to update
        :param name: New name for the portfolio
        :param description: New description for the application
        :return:
        """

    @POST(API_VIEWS_ADD_APPLICATION_VIEW)
    def add_application(self, application, portfolio):
        """
        SINCE 9.3
        Add an existing application to a portfolio.

        :param application: Key of the application to be added
        :param portfolio: Key of the portfolio where the application will be added
        :return:
        """

    @POST(API_VIEWS_ADD_APPLICATION_BRANCH_VIEW)
    def add_application_branch(self, application, branch, key):
        """
        SINCE 9.3
        Add a branch of an application selected in a portfolio.

        :param application: Key of the application
        :param branch: Key of the branch
        :param key: Key of the portfolio
        :return:
        """

    @POST(API_VIEWS_ADD_PORTFOLIO_VIEW)
    def add_portfolio(self, portfolio, reference):
        """
        SINCE 9.3
        Add an existing portfolio to the structure of another portfolio.

        :param portfolio: Key of the portfolio where a reference will be added
        :param reference: Key of the portfolio to be added
        :return:
        """

    @POST(API_VIEWS_ADD_PROJECT_BRANCH_VIEW)
    def add_project_branch(self, project, branch, key):
        """
        SINCE 9.2
        Add a branch of a project selected in a portfolio.

        :param project: Key of the project
        :param branch: Key of the branch
        :param key: Key of the portfolio
        :return:
        """

    @GET(API_VIEWS_APPLICATIONS_VIEW)
    def list_applications(self, portfolio):
        """
        SINCE 9.3
        List applications which the user has access to that can be added to a portfolio.

        :param portfolio: Key of the would-be parent portfolio
        :return:
        """

    @GET(API_VIEWS_PORTFOLIOS_VIEW)
    def list_portfolios(self, portfolio):
        """
        SINCE 9.3
        List portfolios that can be referenced.

        :param portfolio: Key of the would-be parent portfolio
        :return:
        """

    @POST(API_VIEWS_REMOVE_APPLICATION_VIEW)
    def remove_application(self, application, portfolio):
        """
        SINCE 9.3
        Remove an application from a portfolio.

        :param application: Key of the application to be removed
        :param portfolio: Portfolio key
        :return:
        """

    @POST(API_VIEWS_REMOVE_APPLICATION_BRANCH_VIEW)
    def remove_application_branch(self, application, branch, key):
        """
        SINCE 9.3
        Remove a branch of an application selected in a portfolio.

        :param application: Key of the project
        :param branch: Key of the branch
        :param key: Key of the portfolio
        :return:
        """

    @POST(API_VIEWS_REMOVE_PORTFOLIO_VIEW)
    def remove_portfolio(self, portfolio, reference):
        """
        SINCE 9.3
        Remove a reference to a portfolio.

        :param portfolio: Portfolio key
        :param reference: Key of the referenced portfolio to be removed
        :return:
        """

    @POST(API_VIEWS_REMOVE_PROJECT_BRANCH_VIEW)
    def remove_project_branch(self, project, branch, key):
        """
        SINCE 9.2
        Remove a branch of a project selected in a portfolio.

        :param project: Key of the project
        :param branch: Key of the branch
        :param key: Key of the portfolio
        :return:
        """

    @POST(API_VIEWS_SET_NONE_MODE_VIEW)
    def set_none_mode(self, portfolio):
        """
        SINCE 9.1
        Set the projects selection mode of a portfolio to none.
        After setting this mode portfolio will not have any projects assigned.
        Requires 'Administrator' permission on the portfolio.

        :param portfolio: Key of the portfolio or sub-portfolio to update
        :return:
        """
