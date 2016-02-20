# -*- coding: utf-8 -*-


class Error(Exception):
    """Base Error class."""
    pass


class APIError(Error):
    pass


class APIConnectionError(Error):
    pass


class ValidationError(Error):
    pass


class AuthorizationError(Error):
    pass
