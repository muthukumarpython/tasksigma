# TaskSigma API Reference

This document provides a detailed reference for the key classes, functions, and methods used in the TaskSigma project. It serves as a guide for developers looking to understand the functionality and usage of the TaskSigma codebase.

## Table of Contents

1. [ReAct Framework](#react-framework)
    - [ReActAgent](#reactagent)
    - [Utility Functions](#utility-functions)
2. [CAMEL Framework](#camel-framework)
    - [CAMELAgent](#camelagent)
    - [Inception Prompting](#inception-prompting)
    - [Task Specification](#task-specification)
3. [Task Management](#task-management)
    - [ExampleTask](#exampletask)
    - [TaskManager](#taskmanager)
4. [Utilities](#utilities)
    - [Logging](#logging)
    - [Data Processing](#data-processing)

---

## ReAct Framework

### ReActAgent

The `ReActAgent` class integrates reasoning and action capabilities into a single agent. It interacts with environments, generates reasoning traces, and performs actions.

- **`__init__(config)`**
    - Initializes the ReActAgent with the given configuration.
    - **Parameters:**
        - `config` (dict): Configuration dictionary including API keys, model settings, and environment details.
    - **Example:**
    ```python
    agent = ReActAgent(config)
    ```

- **`reason(prompt)`**
    - Generates a reasoning trace based on the provided prompt.
    - **Parameters:**
        - `prompt` (str): The input prompt for generating reasoning.
    - **Returns:** `str` - The reasoning trace.
    - **Example:**
    ```python
    reasoning = agent.reason("How can we optimize our workflow?")
    ```

- **`act(action)`**
    - Performs an action based on the reasoning, such as querying an API.
    - **Parameters:**
        - `action` (str): The action to be performed.
    - **Returns:** `dict` - The result of the action.
    - **Example:**
    ```python
    result = agent.act("Query the database for recent metrics.")
    ```

- **`run(prompt)`**
    - Executes the full reasoning and acting cycle.
    - **Parameters:**
        - `prompt` (str): The initial prompt to start the reasoning process.
    - **Returns:** `dict` - The final result after reasoning and acting.
    - **Example:**
    ```python
    result = agent.run("How do we increase team productivity?")
    ```

### Utility Functions

#### `process_environment(environment_data)`

Processes raw environment data to prepare it for reasoning.

- **Parameters:**
    - `environment_data` (dict): Raw data received from the environment.
- **Returns:** `str` - Formatted environment data.
- **Example:**
```python
processed_data = process_environment(raw_data)
