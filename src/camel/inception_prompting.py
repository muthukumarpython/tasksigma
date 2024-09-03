# tasksigma/camel/inception_prompting.py

import logging

def generate_inception_prompt(user_role, assistant_role, prompt_config):
    """
    Generates an inception prompt for the role-playing session, setting the context and roles
    for the user and assistant agents.

    Args:
        user_role (str): The role assigned to the user agent.
        assistant_role (str): The role assigned to the assistant agent.
        prompt_config (dict): Configuration for the prompt, including the task and word limit.

    Returns:
        str: The generated inception prompt.
    """
    task_description = prompt_config.get('task', 'Complete a collaborative task.')
    word_limit = prompt_config.get('word_limit', 100)

    prompt = (
        f"Task: {task_description}\n"
        f"User Role: {user_role}\n"
        f"Assistant Role: {assistant_role}\n"
        f"Instructions: You will work together to complete the task described above. "
        f"The assistant will follow the user's instructions. "
        f"Please keep your responses concise and within {word_limit} words."
    )

    logging.info(f"Inception prompt generated: {prompt}")
    return prompt

class RolePlayingSession:
    """
    Manages a role-playing session between user and assistant agents.
    """

    def __init__(self, user_agent, assistant_agent):
        """
        Initializes the RolePlayingSession with user and assistant agents.

        Args:
            user_agent: The agent representing the user role.
            assistant_agent: The agent representing the assistant role.
        """
        self.user_agent = user_agent
        self.assistant_agent = assistant_agent
        self.conversation_history = []
        logging.info("Role-playing session initialized.")

    def start(self, initial_prompt):
        """
        Starts the role-playing session using the provided initial prompt.

        Args:
            initial_prompt (str): The initial prompt to start the conversation.

        Returns:
            list: The conversation history after the session completes.
        """
        logging.info("Starting role-playing session...")
        self.conversation_history.append(("Initial Prompt", initial_prompt))
        
        # Example of a basic interaction loop
        for _ in range(20):  # Limiting to 20 rounds for this example
            user_instruction = self.user_agent.generate_instruction(self.conversation_history)
            self.conversation_history.append(("User Instruction", user_instruction))
            logging.info(f"User instruction: {user_instruction}")

            assistant_response = self.assistant_agent.generate_response(user_instruction)
            self.conversation_history.append(("Assistant Response", assistant_response))
            logging.info(f"Assistant response: {assistant_response}")

            # Check for termination conditions (e.g., a special token or instruction)
            if "<CAMEL_TASK_DONE>" in assistant_response:
                logging.info("Termination token found. Ending session.")
                break

        logging.info("Role-playing session completed.")
        return self.conversation_history

def generate_instruction(conversation_history):
    """
    Generates the next instruction from the user agent based on the conversation history.

    Args:
        conversation_history (list): The history of the conversation so far.

    Returns:
        str: The generated user instruction.
    """
    # Placeholder implementation: This should interact with the LLM to generate real instructions
    return f"Instruction based on history: {conversation_history}"

def generate_response(instruction):
    """
    Generates the assistant agent's response to the given instruction.

    Args:
        instruction (str): The instruction from the user agent.

    Returns:
        str: The generated assistant response.
    """
    # Placeholder implementation: This should interact with the LLM to generate real responses
    return f"Response to instruction: {instruction}"
