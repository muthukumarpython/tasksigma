import sys
import logging
from camel.camel_agent import CAMELAgent
from react.react_agent import ReActAgent
from tasks.task_manager import TaskManager
from utils.logging import setup_logging
from config import config_loader

def main():
    # Setup logging
    setup_logging()
    logging.info("TaskSigma project started.")

    # Load configuration
    config = config_loader.load_config('src/config/config.yaml')
    logging.info(f"Loaded configuration: {config}")

    # Initialize Task Manager
    task_manager = TaskManager(config)

    # Initialize ReAct and CAMEL agents based on configuration
    if config['use_react']:
        logging.info("Initializing ReAct agent...")
        react_agent = ReActAgent(config['react'])
        task_manager.register_agent(react_agent)
    
    if config['use_camel']:
        logging.info("Initializing CAMEL agent...")
        camel_agent = CAMELAgent(config['camel'])
        task_manager.register_agent(camel_agent)
    
    # Execute the specified task
    task_name = config['task_name']
    logging.info(f"Starting task: {task_name}")
    task_manager.execute_task(task_name)

    logging.info("Task completed successfully.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        sys.exit(1)
