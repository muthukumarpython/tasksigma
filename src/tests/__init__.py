# tasksigma/src/tests/__init__.py

"""
This package contains the unit tests for the TaskSigma project.

The tests module includes:
- test_react.py: Tests for the ReAct agent and its related functionalities.
- test_camel.py: Tests for the CAMEL agent and its related functionalities.
- test_tasks.py: Tests for the task management system and specific task implementations.
"""

from .test_react import TestReActAgent
from .test_camel import TestCAMELAgent
from .test_tasks import TestTaskManager, TestExampleTask

__all__ = [
    "TestReActAgent",
    "TestCAMELAgent",
    "TestTaskManager",
    "TestExampleTask",
]
