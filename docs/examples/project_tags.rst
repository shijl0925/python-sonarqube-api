================
api/project_tags
================

Manage project tags.
--------------------

Examples
--------

Search tags::

    project_tags = sonar.project_tags.search_project_tags()

Set tags on a project.::

    sonar.project_tags.set_project_tags(project="my_project", tags="finance,offshore")

