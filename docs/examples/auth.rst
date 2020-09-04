==================
api/authentication
==================

Handle authentication.
----------------------

Examples
--------

authenticate a user::

    sonar.auth.authenticate_user(login="kevin", password="xxx")

logout a user::

    sonar.auth.logout_user()

check credentials::

    result = sonar.auth.check_credentials()

