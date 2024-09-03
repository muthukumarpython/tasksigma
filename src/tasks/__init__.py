# tasksigma/tasks/__init__.py

"""
This package contains the task definitions and management functionality for the TaskSigma project.

The tasks module is responsible for defining specific tasks that the agents (ReAct and CAMEL) will execute.
It includes the implementation of example tasks and a task management system to coordinate task execution.

Modules included:
- example_task.py: An example task implementation to demonstrate the integration of ReAct and CAMEL agents.
- task_manager.py: Manages the execution of tasks, including coordinating between different agents and handling task flow.
"""

from .example_task import ExampleTask
from .task_manager import TaskManager

__all__ = [
    "ExampleTask",
    "TaskManager",
]
