# tasksigma/src/tests/test_camel.py

import unittest
from camel.camel_agent import CAMELAgent
from camel.inception_prompting import generate_inception_prompt
from camel.task_specifier import specify_task

class TestCAMELAgent(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment for CAMELAgent tests.
        """
        self.config = {
            'api_key': 'test_api_key',
            'model': 'gpt-4',
            'temperature': 0.7,
            'max_tokens': 1500,
            'agent_name': 'TestCAMELAgent',
            'role_play': {
                'user_role': 'TestUser',
                'assistant_role': 'TestAssistant',
                'inception_prompt': {
                    'task': 'Test Task Description',
                    'word_limit': 50
                }
            },
            'communication_protocol': {
                'message_format': "Instruction: <YOUR_INSTRUCTION>\nInput: <YOUR_INPUT>",
                'response_format': "Solution: <YOUR_SOLUTION>\nNext request."
            },
            'termination_conditions': {
                'max_rounds': 5,
                'success_token': '<CAMEL_TASK_DONE>'
            }
        }
        self.agent = CAMELAgent(self.config)

    def test_start_role_play(self):
        """
        Test the role-playing session of the CAMELAgent.
        """
        result = self.agent.start_role_play()
        self.assertIsInstance(result, dict)
        self.assertIn('conversation_history', result)
        self.assertIn('final_output', result)

class TestInceptionPrompting(unittest.TestCase):
    def test_generate_inception_prompt(self):
        """
        Test the generation of inception prompts.
        """
        user_role = "Developer"
        assistant_role = "AI Assistant"
        prompt_config = {
            'task': 'Develop a new feature',
            'word_limit': 50
        }
        prompt = generate_inception_prompt(user_role, assistant_role, prompt_config)
        self.assertIsInstance(prompt, str)
        self.assertIn(user_role, prompt)
        self.assertIn(assistant_role, prompt)
        self.assertIn(prompt_config['task'], prompt)

class TestTaskSpecifier(unittest.TestCase):
    def test_specify_task(self):
        """
        Test the task specification function.
        """
        base_task = "Analyze the current system"
        word_limit = 100
        detailed_task = specify_task(base_task, word_limit)
        self.assertIsInstance(detailed_task, str)
        self.assertIn(base_task, detailed_task)
        self.assertIn(str(word_limit), detailed_task)

if __name__ == '__main__':
    unittest.main()
