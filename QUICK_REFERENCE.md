# Quick Reference Guide

## 🚀 Getting Started

```bash
# Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run tests
pytest

# Run app
python main.py
```

## 📝 Code Patterns

### Logging
```python
from src.logger import logger

logger.debug("Detailed debug info")
logger.info("General information")
logger.warning("Warning message")
logger.error("Error occurred")
logger.exception("Error with traceback")
```

### Configuration
```python
from src.config import (
    CACHE_DIR,
    COMPUTED_DATA_DIR,
    DEFAULT_YEAR,
    DEFAULT_ROUND,
    PLAYBACK_SPEEDS
)
```

### Exceptions
```python
from src.exceptions import (
    SessionLoadError,
    TelemetryError,
    CacheError,
    ConfigurationError
)

try:
    # Your code
    if error_condition:
        raise SessionLoadError("Descriptive message")
except SessionLoadError as e:
    logger.error(f"Failed: {e}")
```

### Testing
```python
# tests/test_feature.py
import pytest

def test_function():
    result = my_function(input)
    assert result == expected

def test_error_handling():
    with pytest.raises(ValueError):
        my_function(invalid_input)
```

## 🔧 Common Commands

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_config.py

# Run with verbose output
pytest -v

# Run with debug logging
export F1_LOG_LEVEL=DEBUG
python main.py

# View logs
tail -f f1_replay.log

# CLI mode
python main.py --cli

# Direct viewer
python main.py --viewer --year 2025 --round 12
```

## 📁 File Locations

```
src/config.py          → Configuration
src/logger.py          → Logging setup
src/exceptions.py      → Custom exceptions
tests/                 → Test suite
f1_replay.log          → Application logs
pytest.ini             → Test configuration
```

## ✅ Checklist for New Features

- [ ] Use logger instead of print
- [ ] Import from config for constants
- [ ] Raise custom exceptions
- [ ] Add error handling
- [ ] Write tests
- [ ] Update documentation
- [ ] Run pytest before commit

## 🐛 Debugging

```bash
# Enable debug logs
export F1_LOG_LEVEL=DEBUG

# Check log file
cat f1_replay.log

# Run specific test
pytest tests/test_config.py::test_default_values -v

# Python debugger
import pdb; pdb.set_trace()
```

## 📚 Documentation

- `README.md` - Project overview
- `IMPROVEMENTS.md` - Technical details
- `CONTRIBUTING.md` - Developer guide
- `BEFORE_AFTER.md` - Code comparisons
- `SUMMARY.md` - Improvement summary

## 🎯 Best Practices

1. **Always use logger** - No print statements
2. **Import from config** - No hardcoded values
3. **Raise custom exceptions** - Clear error types
4. **Write tests** - Cover new functionality
5. **Handle errors** - Try-catch critical operations
6. **Document changes** - Update relevant docs

## 🔗 Quick Links

- Tests: `pytest`
- Logs: `f1_replay.log`
- Config: `src/config.py`
- Exceptions: `src/exceptions.py`
