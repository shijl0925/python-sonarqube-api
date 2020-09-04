=============
api/favorites
=============

Manage user favorites.
----------------------

Examples
--------
Search for the authenticated user favorites::

    favorites = list(sonar.favorites.search_favorites())

Add a component (project, file etc.) as favorite for the authenticated user::

    sonar.favorites.add_component_to_favorites(component="my_project")

or::

    sonar.favorites.add_component_to_favorites(component="my_project:/src/foo/Bar.php")

Remove a component (project, directory, file etc.) as favorite for the authenticated user::

    sonar.favorites.remove_component_from_favorites(component="my_project")

or::

    sonar.favorites.remove_component_from_favorites(component="my_project:/src/foo/Bar.php")

