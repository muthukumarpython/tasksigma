# tasksigma/tasks/example_task.py

import logging
from react.react_agent import ReActAgent
from camel.camel_agent import CAMELAgent

class ExampleTask:
    """
    ExampleTask demonstrates how to set up and execute a task using both the ReAct and CAMEL agents.
    This task showcases the integration of reasoning, action, and collaborative problem-solving.
    """

    def __init__(self, config):
        """
        Initializes the ExampleTask with the given configuration.

        Args:
            config (dict): Configuration parameters for the task, including settings for the ReAct and CAMEL agents.
        """
        self.config = config
        self.react_agent = ReActAgent(config['react'])
        self.camel_agent = CAMELAgent(config['camel'])
        logging.info("ExampleTask initialized with ReAct and CAMEL agents.")

    def run(self):
        """
        Executes the task by coordinating between the ReAct and CAMEL agents.
        This method demonstrates how both agents can work together to complete a task.
        """
        logging.info("Starting ExampleTask...")

        # Example of using ReAct agent for reasoning and action
        initial_prompt = "How can we improve the efficiency of our task execution?"
        logging.info(f"Running ReAct agent with prompt: {initial_prompt}")
        react_result = self.react_agent.run(initial_prompt)
        logging.info(f"ReAct agent result: {react_result}")

        # Use the result from ReAct agent as an input for CAMEL agent
        task_prompt = react_result['reasoning']
        logging.info(f"Using ReAct result as input for CAMEL agent with prompt: {task_prompt}")
        camel_result = self.camel_agent.start_role_play()
        logging.info(f"CAMEL agent final output: {camel_result['final_output']}")

        # Aggregate and return the results
        result = {
            "react_result": react_result,
            "camel_result": camel_result
        }
        logging.info("ExampleTask completed.")
        return result
