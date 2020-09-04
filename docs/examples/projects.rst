============
api/projects
============

Manage project existence.
-------------------------

Examples
--------

Search for projects or views to administrate them.::

    projects = list(sonar.projects.search_projects())

Create a project.::

    sonar.projects.create_project(project="my_project", name="my project", visibility="private")

Delete a project.::

    sonar.projects.delete_project(project="my_project")

Delete one or several projects.::

    sonar.projects.bulk_delete_projects(projects="my_project,another_project")

Update a project or module key and all its sub-components keys.::

    sonar.projects.update_project_key(previous_project_key="my_old_project", new_project_key="my_new_project")

Updates visibility of a project.::

    sonar.projects.update_project_visibility(project="my_project", visibility="private")

