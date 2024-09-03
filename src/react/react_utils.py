# tasksigma/react/react_utils.py

import logging

def process_environment(environment_data):
    """
    Processes data from the external environment to prepare it for reasoning.

    Args:
        environment_data (dict): The raw data received from the environment.

    Returns:
        str: A formatted string representing the essential information extracted
             from the environment data.
    """
    logging.info("Processing environment data...")
    # Extract relevant information and format it
    processed_data = "Processed data: " + ", ".join(
        [f"{key}: {value}" for key, value in environment_data.items()]
    )
    logging.info(f"Environment data processed: {processed_data}")
    return processed_data


def format_reasoning(reasoning_trace):
    """
    Formats the reasoning trace to be more readable or suitable for the next action.

    Args:
        reasoning_trace (str): The raw reasoning trace generated by the model.

    Returns:
        str: A formatted version of the reasoning trace.
    """
    logging.info("Formatting reasoning trace...")
    # Example of formatting: trimming whitespace and adding context
    formatted_trace = reasoning_trace.strip()
    formatted_trace = f"Reasoned: {formatted_trace}"
    logging.info(f"Formatted reasoning trace: {formatted_trace}")
    return formatted_trace


def validate_action(action):
    """
    Validates the proposed action before it is executed.

    Args:
        action (str): The action to be validated.

    Returns:
        bool: True if the action is valid, False otherwise.
    """
    logging.info(f"Validating action: {action}")
    # Simple validation example: Check if action is non-empty and not too long
    if not action or len(action) > 200:
        logging.warning("Action validation failed.")
        return False
    logging.info("Action validation succeeded.")
    return True


def log_interaction(reasoning_trace, action_result):
    """
    Logs the interaction details including the reasoning and the result of the action.

    Args:
        reasoning_trace (str): The reasoning generated by the model.
        action_result (dict): The result of the action performed in the environment.
    """
    logging.info("Logging interaction...")
    interaction_details = (
        f"Reasoning Trace: {reasoning_trace}\n"
        f"Action Result: {action_result}\n")
 
