"""Custom exceptions for F1 Race Replay."""

class F1ReplayError(Exception):
    """Base exception for F1 Race Replay."""
    pass

class SessionLoadError(F1ReplayError):
    """Raised when session data cannot be loaded."""
    pass

class TelemetryError(F1ReplayError):
    """Raised when telemetry data is invalid or missing."""
    pass

class CacheError(F1ReplayError):
    """Raised when cache operations fail."""
    pass

class ConfigurationError(F1ReplayError):
    """Raised when configuration is invalid."""
    pass
