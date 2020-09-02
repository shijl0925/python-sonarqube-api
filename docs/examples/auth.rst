==================
api/authentication
==================

Handle authentication.
______________________

Examples
--------

authenticate a user::

    sonar.auth.authenticate_user(login="kevin", password="xxx")

logout a user::

    sonar.auth.logout_user()

check credentials::

    print(sonar.auth.check_credentials())

