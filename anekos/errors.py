class NekoException(Exception):
    """Base class for exceptions."""
    pass


class NoResponse(NekoException):
    """The API didn't return anything or got no response."""
    pass
