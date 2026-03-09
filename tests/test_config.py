"""Tests for configuration module."""
import pytest
from pathlib import Path
from src.config import (
    PROJECT_ROOT,
    CACHE_DIR,
    COMPUTED_DATA_DIR,
    DEFAULT_YEAR,
    DEFAULT_PLAYBACK_SPEED,
    PLAYBACK_SPEEDS,
    ensure_directories
)

def test_project_paths_exist():
    """Test that project paths are valid Path objects."""
    assert isinstance(PROJECT_ROOT, Path)
    assert isinstance(CACHE_DIR, Path)
    assert isinstance(COMPUTED_DATA_DIR, Path)

def test_default_values():
    """Test default configuration values."""
    assert isinstance(DEFAULT_YEAR, int)
    assert DEFAULT_YEAR > 2000
    assert DEFAULT_PLAYBACK_SPEED in PLAYBACK_SPEEDS
    assert len(PLAYBACK_SPEEDS) > 0

def test_ensure_directories():
    """Test directory creation."""
    ensure_directories()
    assert CACHE_DIR.exists()
    assert COMPUTED_DATA_DIR.exists()
