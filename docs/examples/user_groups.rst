===============
api/user_groups
===============

Manage user groups.
___________________

Examples
--------

Search for user groups::

    user_groups = sonar.user_groups.search_user_groups()

Create a group.::

    sonar.user_groups.create_group(group_name="sonar-users-test", description="Default group for new users")

Delete a group. The default groups cannot be deleted.::

    sonar.user_groups.delete_group(group_name="sonar-users-test")

Update a group.::

    sonar.user_groups.update_group(group_id=42, group_name="my-group", description="Default group for new users")

Add a user to a group.::

    sonar.user_groups.add_user_to_group(group_name="my-group", user_login="kevin")

Remove a user from a group.::

    sonar.user_groups.remove_user_from_group(group_name="my-group", user_login="kevin")

Search for users with membership information with respect to a group.::

    users = sonar.user_groups.search_users_belong_to_group(group_name="my-group")

