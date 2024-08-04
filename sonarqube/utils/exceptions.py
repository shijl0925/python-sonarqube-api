class ClientError(Exception):
    """
    client error

    """


class ServerError(Exception):
    """
    server error

    """


class AuthError(ClientError):
    """
    authorization error

    """


class ValidationError(ClientError):
    """
    validation error

    """


class NotFoundError(ClientError):
    """
    not found error

    """
