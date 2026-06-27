class AIException(Exception):
    """Base AI Exception"""
    pass


class RateLimitException(AIException):
    """Raised when API rate limit is exceeded."""
    pass


class InvalidResponseException(AIException):
    """Raised when the AI returns an invalid response."""
    pass