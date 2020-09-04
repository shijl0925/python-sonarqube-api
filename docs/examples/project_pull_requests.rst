=========================
api/project_pull_requests
=========================

Manage pull request (only available when the Branch plugin is installed).
-------------------------------------------------------------------------

Examples
--------

List the pull requests of a project.::

    project_pull_requests = sonar.project_pull_requests.search_project_pull_requests(project="my_project")

Delete a pull request.::

    sonar.project_pull_requests.delete_project_pull_requests(project="my_project", pull_request_id=1543)

