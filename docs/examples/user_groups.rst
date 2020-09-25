===============
api/user_groups
===============

Manage user groups.
-------------------

Examples
--------

Search for user groups::

    user_groups = list(sonar.user_groups.search_user_groups())

Create a group.::

    sonar.user_groups.create_group(name="sonar-users-test", description="Default group for new users")

Delete a group. The default groups cannot be deleted.::

    sonar.user_groups.delete_group(name="sonar-users-test")

Update a group.::

    sonar.user_groups.update_group(id=42, name="my-group", description="Default group for new users")

Add a user to a group.::

    sonar.user_groups.add_user_to_group(name="my-group", login="kevin")

Remove a user from a group.::

    sonar.user_groups.remove_user_from_group(name="my-group", login="kevin")

Search for users with membership information with respect to a group.::

    users = list(sonar.user_groups.search_users_belong_to_group(name="my-group"))

