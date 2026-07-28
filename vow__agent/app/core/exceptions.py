"""Application exception hierarchy.

Typed exceptions let the agent graph branch on failure rather than
parsing error strings.
"""


class VowAgentError(Exception):
    """Base for everything this service raises."""


class ConfigurationError(VowAgentError):
    """Something required is missing or malformed at startup."""


class VowApiError(VowAgentError):
    """A call to the VOW platform API failed."""

    def __init__(self, message: str, status_code: int | None = None, endpoint: str | None = None):
        super().__init__(message)
        self.status_code = status_code
        self.endpoint = endpoint


class VowAuthError(VowApiError):
    """Authentication or authorisation against the VOW API failed."""


class AdvertiserContextMissingError(VowAgentError):
    """A scoped call was attempted without advertiser context.

    Fail closed: we never default to an advertiser.
    """


class GroundingError(VowAgentError):
    """An identifier could not be validated against the grounded registry."""