# tasksigma/camel/camel_agent.py

import logging
from .inception_prompting import generate_inception_prompt
from .task_specifier import specify_task

class CAMELAgent:
    """
    CAMELAgent is responsible for enabling autonomous cooperation between communicative agents,
    allowing them to collaborate and complete tasks through structured role-playing scenarios.
    """

    def __init__(self, config):
        """
        Initializes the CAMELAgent with the given configuration.

        Args:
            config (dict): Configuration parameters for the agent, including API keys,
                           model settings, role assignments, and communication protocols.
        """
        self.api_key = config.get('api_key')
        self.model = config.get('model', 'gpt-4')
        self.temperature = config.get('temperature', 0.7)
        self.max_tokens = config.get('max_tokens', 1500)
        self.agent_name = config.get('agent_name', 'CAMELAgent')
        self.user_role = config['role_play'].get('user_role', 'User')
        self.assistant_role = config['role_play'].get('assistant_role', 'Assistant')
        self.inception_prompt_config = config['role_play'].get('inception_prompt', {})
        self.communication_protocol = config.get('communication_protocol', {})
        self.termination_conditions = config.get('termination_conditions', {})
        logging.info(f"{self.agent_name} initialized with model {self.model} for roles {self.user_role} and {self.assistant_role}")

    def start_role_play(self):
        """
        Starts a role-playing session between the user agent and the assistant agent
        based on the specified task and roles.
        
        Returns:
            dict: The results of the role-playing session, including the conversation and final output.
        """
        logging.info("Starting role-playing session...")
        
        # Generate the inception prompt for the role-playing session
        prompt = generate_inception_prompt(self.user_role, self.assistant_role, self.inception_prompt_config)
        logging.info(f"Inception prompt generated: {prompt}")
        
        # Specify the task to be completed by the agents
        task_details = specify_task(self.inception_prompt_config['task'], self.inception_prompt_config.get('word_limit', 100))
        logging.info(f"Specified task: {task_details}")
        
        # Initialize conversation history
        conversation_history = []

        # Start the communication loop between the agents
        try:
            while not self._check_termination(conversation_history):
                user_instruction = self._generate_instruction(conversation_history)
                assistant_response = self._generate_response(user_instruction)
                conversation_history.append((user_instruction, assistant_response))
                # logging.info(f"User instruction: {user_instruction}")
                # logging.info(f"Assistant response: {assistant_response}")
        except Exception as e:
            logging.error(f"An error occurred in communication loop: {str(e)}")
            raise
        # while not self._check_termination(conversation_history):
        #     user_instruction = self._generate_instruction(conversation_history)
        #     assistant_response = self._generate_response(user_instruction)
        #     conversation_history.append((user_instruction, assistant_response))
        #     # logging.info(f"User instruction===>: {user_instruction}")
        #     # logging.info(f"Assistant response===>: {assistant_response}")

        # logging.info("Role-playing session completed.",conversation_history)
        return {
            "conversation_history": conversation_history,
            "final_output": conversation_history[-1] if conversation_history else None
        }

    def _generate_instruction(self, conversation_history):
        """
        Generates the next instruction from the user agent based on the conversation history.
        """
        try:
            # Replace this with actual logic for generating instructions
            instruction = f"Instruction based on history: {conversation_history}"
            # logging.debug(f"Generated instruction: {instruction}")
            return instruction
        except Exception as e:
            logging.error(f"Error generating instruction: {str(e)}")
            raise

    def _generate_response(self, instruction):
        """
        Generates the assistant agent's response to the given instruction.
        """
        try:
            # Replace this with actual logic for generating responses
            response = f"Response to instruction: {instruction}"
            # logging.debug(f"Generated response: {response}")
            return response
        except Exception as e:
            logging.error(f"Error generating response: {str(e)}")
            raise

    def _check_termination(self, conversation_history):
        """
        Checks if the termination conditions for the role-playing session have been met.

        Args:
            conversation_history (list): The history of the conversation so far.

        Returns:
            bool: True if the session should be terminated, False otherwise.
        """
        # Example termination check based on the number of conversation rounds
        # max_rounds = self.termination_conditions.get('max_rounds', 20)
        # if len(conversation_history) >= max_rounds:
        #     logging.info("Termination condition met: Maximum rounds reached.")
        #     return True
        
        # # Check for a specific termination token in the conversation
        # success_token = self.termination_conditions.get('success_token', '<CAMEL_TASK_DONE>')
        # if any(success_token in response for _, response in conversation_history):
        #     logging.info(f"Termination condition met: Success token '{success_token}' found.")
        #     return True
        
        # return False
    
        return len(conversation_history) > 10  # Example: end after 10 exchanges
