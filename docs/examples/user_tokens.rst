===============
api/user_tokens
===============

List, create, and delete a user's access tokens.
________________________________________________

Examples
--------

Generate a user access token.::

    user_token = sonar.user_tokens.generate_user_token("Project scan on Travis")

Revoke a user access token.::

    sonar.user_tokens.revoke_user_token("Project scan on Travis")

List the access tokens of a user.::

    user_tokens = sonar.user_tokens.search_user_tokens(user_login="kevin")

