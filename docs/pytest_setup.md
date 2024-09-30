# Setup Pytest for Testing Project
In project i use 'poetry' package manager.

```bash
poetry add --dev pytest
```

Your possible project structure:

```txt
my-project/
├── my_project/
│   ├── tasks/
│   │   └── homework/
│   │       └── solution.py
├── tests/
│   ├── tasks/
│   │   └── homework/
│   │       └── test_solution.py
└── pyproject.toml
```

```python
# my_project/tasks/homework/solution.py

def add(a, b):
    return a + b
```

```python
# tests/tasks/homework/test_solution.py
from my_project.tasks.homework.solution import add

def test_add():
    assert add(1, 2) == 3
```

Setup Pytest in `pyproject.toml`:
```toml
[tool.pytest.ini_options]
pythonpath = ["."]
```

Setup `pytest.ini`:
```ini
[pytest]
# dir with tests
testpaths = tests

# root directory
pythonpath = .
```

Run tests:

```bash
# Run all tests
poetry run pytest

# Run specific test
poetry run pytest tests/tasks/homework/test_solution.py
```
