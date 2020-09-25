=================
api/project_links
=================

Manage projects links.
----------------------

Examples
--------

Create a new project link.::

    sonar.project_links.create_project_link(projectKey="my_project", name="Custom", url="http://example.com")

Delete existing project link.::

    sonar.project_links.delete_project_link(id=17)

List links of a project.::

    project_links = sonar.project_links.search_project_links(projectKey="my_project")

