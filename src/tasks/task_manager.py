# tasksigma/src/tasks/task_manager.py

import logging
from tasks.example_task import ExampleTask

class TaskManager:
    """
    TaskManager is responsible for managing the execution of tasks in the TaskSigma project.
    It coordinates the initialization and execution of tasks, including those using the ReAct
    and CAMEL agents.
    """

    def __init__(self, config):
        """
        Initializes the TaskManager with the given configuration.

        Args:
            config (dict): Configuration parameters for the TaskManager, including task-specific settings.
        """
        self.config = config
        self.tasks = {
            "example_task": ExampleTask
            # Additional tasks can be registered here
        }
        self.agents = []  # New attribute to store agents
        logging.info("TaskManager initialized with available tasks.")

    def run(self):
        """
        Executes the task.

        Returns:
            dict: The result of the task execution.
        """
        # Implement the task execution logic here
        pass    

    def register_task(self, task_name, task_class):
        """
        Registers a new task with the TaskManager.

        Args:
            task_name (str): The name of the task to register.
            task_class (class): The class representing the task.
        """
        self.tasks[task_name] = task_class
        logging.info(f"Task '{task_name}' registered.")

    def register_agent(self, agent):
        """
        Registers a new agent with the TaskManager.

        Args:
            agent (object): The agent instance to register.
        """
        self.agents.append(agent)
        logging.info(f"Agent '{type(agent).__name__}' registered.")    

    def execute_task(self, task_name):
        if task_name not in self.tasks:
            logging.error(f"Task '{task_name}' not found.")
            raise ValueError(f"Task '{task_name}' is not registered in TaskManager.")
        
        logging.info(f"Executing task: {task_name}")
        task_class = self.tasks[task_name]

        # Get task-specific configuration
        task_config = self.config.get('tasks', {}).get(task_name, None)
        # logging.info(f"task_config: {task_config}")
        if task_config is None:
            logging.error(f"Configuration for task '{task_name}' not found in config.")
            raise ValueError(f"Configuration for task '{task_name}' is missing.")
        
        # Ensure `react` and `camel` configurations are included
        task_config.update({
            'react': self.config.get('react', {}),
            'camel': self.config.get('camel', {})
        })

        try:
            # Initialize the task with the full configuration including agents
            task_instance = task_class(task_config)
        except TypeError as e:
            logging.error(f"Error initializing task class '{task_class.__name__}': {str(e)}")
            raise
        
        logging.info(f"Task instance created: {task_instance}")
        
        # Pass registered agents to the task instance if applicable
        for agent in self.agents:
            if hasattr(task_instance, 'add_agent'):
                task_instance.add_agent(agent)
        
        result = task_instance.run()
        logging.info(f"Task '{task_name}' execution completed.")
        return result



