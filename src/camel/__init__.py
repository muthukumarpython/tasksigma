# tasksigma/camel/__init__.py

"""
This package contains the implementation of the CAMEL (Communicative Agents for "Mind" Exploration of Large Language Model Society) framework
for the TaskSigma project.

The CAMEL framework is designed to enable autonomous cooperation between communicative agents, allowing them to collaborate and complete tasks
through structured role-playing scenarios.

Modules included:
- camel_agent.py: Core implementation of the CAMEL agent.
- inception_prompting.py: Functions and classes for generating inception prompts that guide the role-playing sessions.
- task_specifier.py: Utilities to specify and detail tasks for the agents based on initial ideas or prompts.
"""

from .camel_agent import CAMELAgent
from .inception_prompting import generate_inception_prompt, RolePlayingSession
from .task_specifier import specify_task, TaskSpecifier

__all__ = [
    "CAMELAgent",
    "generate_inception_prompt",
    "RolePlayingSession",
    "specify_task",
    "TaskSpecifier",
]
