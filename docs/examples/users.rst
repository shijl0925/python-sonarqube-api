=========
api/users
=========

Manage users.
-------------

Examples
--------

Get a list of active users.::

    users = list(sonar.users.search_users())

Create a user.::

    sonar.users.create_user(login="sonar", name="SonarQube", password="sonar@123")

Update a user.::

    sonar.users.update_user(login="sonar", email="sonar@company.com")

Deactivate a user.::

    sonar.users.deactivate_user(login="new_sonar")

Update a user login. A login can be updated many times.::

    sonar.users.update_user_login('sonar', 'new_sonar')

