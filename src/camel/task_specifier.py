# tasksigma/camel/task_specifier.py

import logging

class TaskSpecifier:
    """
    TaskSpecifier is responsible for converting general ideas into specific, detailed tasks
    that agents can work on. This involves breaking down high-level objectives into clear,
    actionable steps.
    """

    def __init__(self, base_task, word_limit=100):
        """
        Initializes the TaskSpecifier with a base task description and optional word limit.

        Args:
            base_task (str): The high-level description of the task.
            word_limit (int): The word limit for the specified task details.
        """
        self.base_task = base_task
        self.word_limit = word_limit
        logging.info(f"TaskSpecifier initialized with base task: '{self.base_task}' and word limit: {self.word_limit}")

    def specify(self):
        """
        Converts the base task into a more detailed and specific task description.

        Returns:
            str: The detailed task specification.
        """
        logging.info("Specifying task...")
        # Example task specification process: Here we simply expand the base task with more details.
        detailed_task = (
            f"Task: {self.base_task}. "
            f"This task requires the following steps to be completed within {self.word_limit} words: "
            "1. Understand the context and objectives. "
            "2. Plan the approach and break down the task into manageable sub-tasks. "
            "3. Execute the sub-tasks sequentially while monitoring progress. "
            "4. Review and validate the results to ensure they meet the objectives."
        )
        logging.info(f"Task specified: {detailed_task}")
        return detailed_task


def specify_task(base_task, word_limit=100):
    """
    A utility function to create a detailed task description from a base task.

    Args:
        base_task (str): The high-level description of the task.
        word_limit (int): The word limit for the specified task details.

    Returns:
        str: The detailed task specification.
    """
    logging.info("Using utility function to specify task...")
    specifier = TaskSpecifier(base_task, word_limit)
    return specifier.specify()
