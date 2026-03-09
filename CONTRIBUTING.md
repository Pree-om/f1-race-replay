# Contributing to F1 Race Replay

Thank you for your interest in contributing! This guide will help you get started.

## Development Setup

1. **Clone and setup:**
   ```bash
   git clone https://github.com/IAmTomShaw/f1-race-replay
   cd f1-race-replay
   python3 -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Run tests:**
   ```bash
   pytest
   ```

3. **Run the application:**
   ```bash
   python main.py
   ```

## Code Standards

### Use the Logger
```python
from src.logger import logger

logger.info("Information message")
logger.warning("Warning message")
logger.error("Error message")
logger.debug("Debug details")
```

### Use Configuration
```python
from src.config import CACHE_DIR, DEFAULT_YEAR

# Access centralized settings
cache_path = CACHE_DIR / "my_cache.pkl"
```

### Handle Errors Properly
```python
from src.exceptions import SessionLoadError

try:
    session = load_session(year, round_number)
    if session is None:
        raise SessionLoadError(f"Session not found: {year} R{round_number}")
except SessionLoadError as e:
    logger.error(f"Failed to load: {e}")
    return None
```

### Write Tests
```python
# tests/test_my_feature.py
import pytest
from src.my_module import my_function

def test_my_function():
    result = my_function(input_data)
    assert result == expected_output

def test_my_function_error():
    with pytest.raises(ValueError):
        my_function(invalid_input)
```

## Pull Request Guidelines

1. **One feature per PR** - Keep changes focused
2. **Write tests** - Add tests for new functionality
3. **Update docs** - Document new features
4. **Follow existing patterns** - Match the codebase style
5. **Test locally** - Run `pytest` before submitting

## Project Structure

```
src/
├── config.py          # Configuration management
├── logger.py          # Logging system
├── exceptions.py      # Custom exceptions
├── f1_data.py         # Data loading and processing
├── run_session.py     # Session execution
├── cli/               # CLI interface
├── gui/               # GUI components
├── interfaces/        # Replay interfaces
├── insights/          # Telemetry windows
└── lib/               # Utilities

tests/                 # Test suite
```

## Common Tasks

### Adding a New Feature

1. Create feature branch: `git checkout -b feature/my-feature`
2. Implement with proper logging and error handling
3. Write tests in `tests/test_my_feature.py`
4. Update documentation
5. Submit PR with description and screenshots

### Fixing a Bug

1. Create bug branch: `git checkout -b fix/bug-description`
2. Add test that reproduces the bug
3. Fix the bug
4. Verify test passes
5. Submit PR referencing the issue

### Improving Performance

1. Profile the code to identify bottlenecks
2. Implement optimization
3. Benchmark before/after
4. Document performance gains in PR

## Debugging

### Enable Debug Logging
```bash
export F1_LOG_LEVEL=DEBUG
python main.py
```

### Check Logs
```bash
tail -f f1_replay.log
```

### Run Specific Tests
```bash
pytest tests/test_config.py -v
pytest -k "test_session" -v
```

## Questions?

- Open an issue on GitHub
- Email: tom@tomshaw.dev
- Check existing issues and PRs first

## Code of Conduct

- Be respectful and constructive
- Focus on the code, not the person
- Help others learn and grow
- Follow the project's vision and roadmap
