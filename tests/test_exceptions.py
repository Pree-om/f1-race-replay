"""Tests for custom exceptions."""
import pytest
from src.exceptions import (
    F1ReplayError,
    SessionLoadError,
    TelemetryError,
    CacheError,
    ConfigurationError
)

def test_base_exception():
    """Test base F1ReplayError."""
    with pytest.raises(F1ReplayError):
        raise F1ReplayError("Test error")

def test_session_load_error():
    """Test SessionLoadError inherits from F1ReplayError."""
    assert issubclass(SessionLoadError, F1ReplayError)
    with pytest.raises(SessionLoadError):
        raise SessionLoadError("Session not found")

def test_telemetry_error():
    """Test TelemetryError inherits from F1ReplayError."""
    assert issubclass(TelemetryError, F1ReplayError)

def test_cache_error():
    """Test CacheError inherits from F1ReplayError."""
    assert issubclass(CacheError, F1ReplayError)

def test_configuration_error():
    """Test ConfigurationError inherits from F1ReplayError."""
    assert issubclass(ConfigurationError, F1ReplayError)
