# tasksigma/src/__init__.py

"""
TaskSigma: A project integrating ReAct and CAMEL frameworks for autonomous task-solving
using Large Language Models (LLMs).

This package contains the core modules and functionality for TaskSigma, including:

- ReAct agent implementation
- CAMEL agent implementation
- Task management system
- Utility functions for data processing and logging
- Configuration management
"""

# Import essential modules for easier access
from .react import ReActAgent
from .camel import CAMELAgent
from .tasks import TaskManager
from .config import config_loader
from .utils import logging

# Define package version
__version__ = "1.0.0"
