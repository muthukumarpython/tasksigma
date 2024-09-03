# tasksigma/react/__init__.py

"""
This package contains the implementation of the ReAct (Reasoning and Acting) framework
for the TaskSigma project.

The ReAct framework integrates reasoning and action-taking capabilities in Large Language Models (LLMs),
allowing them to interact with environments, perform tasks, and update their reasoning based on observations.

Modules included:
- react_agent.py: Core implementation of the ReAct agent.
- react_utils.py: Utility functions to support ReAct agent operations.
"""

from .react_agent import ReActAgent
from .react_utils import process_environment, format_reasoning

__all__ = [
    "ReActAgent",
    "process_environment",
    "format_reasoning",
]
