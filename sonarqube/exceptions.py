class ClientError(Exception):
    pass


class ServerError(Exception):
    pass


class AuthError(ClientError):
    pass


class ValidationError(ClientError):
    pass
