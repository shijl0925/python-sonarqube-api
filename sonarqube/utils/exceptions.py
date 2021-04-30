class ClientError(Exception):
    """
    client error

    """

    pass


class ServerError(Exception):
    """
    server error

    """

    pass


class AuthError(ClientError):
    """
    authorization error

    """

    pass


class ValidationError(ClientError):
    """
    validation error

    """

    pass


class NotFoundError(ClientError):
    """
    not found error

    """
    pass
