==============
api/components
==============

Get information about a component (file, directory, project, ...) and its ancestors or descendants. Update a project or module key.
-----------------------------------------------------------------------------------------------------------------------------------

Examples
--------


Returns a component (file, directory, project, view) and its ancestors. The ancestors are ordered from the parent to the root project.::


    component = sonar.components.get_project_component_and_ancestors("my_project")

Search for components::

    components = list(sonar.components.search_components(qualifiers="TRK", language="java"))


Navigate through components based on the chosen strategy. When limiting search with the q parameter, directories are not returned.::

    components_tree = list(sonar.components.get_components_tree(component="my_project", qualifiers="TRK"))

