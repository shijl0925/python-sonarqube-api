====================
api/project_branches
====================

Manage branch (only available when the Branch plugin is installed)
__________________________________________________________________

Examples
--------

List the branches of a project.::

    branches = sonar.project_branches.search_project_branches(project="my-project")

Delete a non-main branch of a project.::

    sonar.project_branches.delete_project_branch(project="my_project", branch="branch1")

Rename the main branch of a project.::

    sonar.project_branches.rename_project_branch(project="my_project", name="branch1")

