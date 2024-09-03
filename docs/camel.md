# CAMEL Framework Documentation

The **CAMEL (Communicative Agents for "Mind" Exploration of Large Language Model Society)** framework is a key component of the TaskSigma project. It is designed to enable autonomous cooperation between communicative agents, allowing them to collaborate on complex tasks through structured role-playing scenarios.

## Overview

CAMEL focuses on:

- **Role-Based Interaction**: Assigning distinct roles to agents, such as "User" and "Assistant," to simulate real-world task-solving scenarios.
- **Inception Prompting**: Guiding agents through their tasks using carefully crafted prompts that set the context and expectations for their interactions.
- **Collaborative Problem Solving**: Enabling agents to communicate and work together to achieve common goals, making decisions collaboratively.

## Components

### 1. **CAMELAgent**

The `CAMELAgent` class is the core implementation of the CAMEL framework. It manages the interactions between agents, ensuring they adhere to their roles and complete tasks effectively.

- **Initialization**:
    - The `CAMELAgent` is initialized with a configuration dictionary that includes role assignments, communication protocols, and termination conditions.
    - Example:
    ```python
    config = {
        'api_key': 'your_api_key',
        'model': 'gpt-4',
        'temperature': 0.7,
        'max_tokens': 1500,
        'role_play': {
            'user_role': 'Product Manager',
            'assistant_role': 'AI Assistant',
            'inception_prompt': {
                'task': 'Develop a new feature',
                'word_limit': 100
            }
        },
        'communication_protocol': {
            'message_format': "Instruction: <YOUR_INSTRUCTION>\nInput: <YOUR_INPUT>",
            'response_format': "Solution: <YOUR_SOLUTION>\nNext request."
        },
        'termination_conditions': {
            'max_rounds': 10,
            'success_token': '<CAMEL_TASK_DONE>'
        }
    }
    agent = CAMELAgent(config)
    ```

- **Role Playing**:
    - The `start_role_play` method initiates a role-playing session where the user and assistant agents interact according to their assigned roles.
    - Example:
    ```python
    result = agent.start_role_play()
    ```

### 2. **Inception Prompting**

Inception prompting is a technique used to guide the agents through their roles. It involves creating structured prompts that define the task, roles, and expected outcomes.

- **`generate_inception_prompt`**:
    - This function generates a prompt that sets up the role-playing session, including the task description and roles.
    - Example:
    ```python
    prompt_config = {
        'task': 'Create a marketing strategy',
        'word_limit': 50
    }
    prompt = generate_inception_prompt('Marketing Manager', 'AI Assistant', prompt_config)
    ```

- **`RolePlayingSession`**:
    - The `RolePlayingSession` class manages the interaction between agents, ensuring they follow the defined protocol and reach a conclusion within the specified limits.
    - Example:
    ```python
    session = RolePlayingSession(user_agent, assistant_agent)
    conversation_history = session.start(initial_prompt)
    ```

### 3. **Task Specification**

The CAMEL framework includes tools for specifying tasks that agents will work on. These tools help in converting high-level ideas into detailed, actionable tasks.

- **`TaskSpecifier`**:
    - The `TaskSpecifier` class is responsible for breaking down a general task description into specific steps that agents can follow.
    - Example:
    ```python
    specifier = TaskSpecifier('Improve customer satisfaction', word_limit=100)
    detailed_task = specifier.specify()
    ```

- **`specify_task`**:
    - A utility function that simplifies the task specification process by providing an easy-to-use interface.
    - Example:
    ```python
    detailed_task = specify_task('Optimize resource allocation', 100)
    ```

## Use Cases

The CAMEL framework is well-suited for tasks that require collaboration between multiple agents with different roles, such as:

- **Product Development**: Where a Product Manager (User) collaborates with an AI Assistant to design and plan a new product feature.
- **Project Management**: Where a Project Manager (User) and AI Assistant work together to create a project timeline and resource allocation plan.
- **Marketing Strategy**: Where a Marketing Manager (User) and AI Assistant develop a comprehensive marketing plan for a new product launch.

## Example Scenario

### Task: Develop a Marketing Strategy

1. **Roles**:
    - User: Marketing Manager
    - Assistant: AI Assistant

2. **Inception Prompt**:
    - "Task: Develop a marketing strategy for the new product launch. The Marketing Manager will lead the strategy development, and the AI Assistant will provide data-driven insights. The final plan should be within 100 words."

3. **Interaction**:
    - The Marketing Manager outlines the initial goals.
    - The AI Assistant suggests data sources and provides insights based on previous campaigns.
    - Together, they refine the strategy, ensuring it aligns with company goals and market trends.

4. **Outcome**:
    - A detailed marketing strategy is produced, incorporating both creative ideas and data-driven recommendations.

## Best Practices

- **Role Clarity**: Clearly define the roles and responsibilities of each agent to ensure smooth collaboration.
- **Prompt Design**: Use precise and structured prompts to guide the agents effectively through the task.
- **Termination Conditions**: Set clear termination conditions to prevent the session from continuing indefinitely and to ensure timely completion of tasks.

## Conclusion

The CAMEL framework in TaskSigma provides a powerful method for enabling collaboration between agents with distinct roles. By leveraging role-playing and structured prompting, CAMEL facilitates complex problem-solving tasks that require the combined expertise of multiple agents.

For more detailed examples and technical information, refer to the source code and unit tests included in the TaskSigma project.
