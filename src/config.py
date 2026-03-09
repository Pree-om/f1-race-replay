"""Configuration management for F1 Race Replay."""
import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
CACHE_DIR = PROJECT_ROOT / ".fastf1-cache"
COMPUTED_DATA_DIR = PROJECT_ROOT / "computed_data"
IMAGES_DIR = PROJECT_ROOT / "images"

# Default settings
DEFAULT_YEAR = 2025
DEFAULT_ROUND = 12
DEFAULT_PLAYBACK_SPEED = 1.0
PLAYBACK_SPEEDS = [0.5, 1.0, 2.0, 4.0]

# UI settings
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
TRACK_WIDTH = 8
DRIVER_CIRCLE_RADIUS = 6

# Performance settings
MAX_CACHE_SIZE_MB = 1000
TELEMETRY_UPDATE_RATE = 60  # Hz

# Logging
LOG_LEVEL = os.getenv("F1_LOG_LEVEL", "INFO")
LOG_FILE = PROJECT_ROOT / "f1_replay.log"

def ensure_directories():
    """Create required directories if they don't exist."""
    CACHE_DIR.mkdir(exist_ok=True)
    COMPUTED_DATA_DIR.mkdir(exist_ok=True)
