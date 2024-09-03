# tasksigma/src/tests/test_tasks.py

import unittest
from tasks.example_task import ExampleTask
from tasks.task_manager import TaskManager

class TestExampleTask(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment for ExampleTask tests.
        """
        self.config = {
            'react': {
                'api_key': 'test_api_key',
                'model': 'gpt-4',
                'temperature': 0.7,
                'max_tokens': 1500,
                'agent_name': 'TestReActAgent',
                'environment': {
                    'type': 'api',
                    'endpoint': 'https://example.com/api',
                    'headers': {
                        'Authorization': 'Bearer test_token'
                    }
                }
            },
            'camel': {
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
        }
        self.task = ExampleTask(self.config)

    def test_run(self):
        """
        Test the execution of the ExampleTask.
        """
        result = self.task.run()
        self.assertIsInstance(result, dict)
        self.assertIn('react_result', result)
        self.assertIn('camel_result', result)
        self.assertIn('reasoning', result['react_result'])
        self.assertIn('result', result['react_result'])
        self.assertIn('conversation_history', result['camel_result'])
        self.assertIn('final_output', result['camel_result'])

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment for TaskManager tests.
        """
        self.config = {
            'example_task': {
                'react': {
                    'api_key': 'test_api_key',
                    'model': 'gpt-4',
                    'temperature': 0.7,
                    'max_tokens': 1500,
                    'agent_name': 'TestReActAgent',
                    'environment': {
                        'type': 'api',
                        'endpoint': 'https://example.com/api',
                        'headers': {
                            'Authorization': 'Bearer test_token'
                        }
                    }
                },
                'camel': {
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
            }
        }
        self.manager = TaskManager(self.config)

    def test_execute_task(self):
        """
        Test the execution of a task using the TaskManager.
        """
        result = self.manager.execute_task('example_task')
        self.assertIsInstance(result, dict)
        self.assertIn('react_result', result)
        self.assertIn('camel_result', result)

    def test_register_task(self):
        """
        Test the registration of a new task in the TaskManager.
        """
        class DummyTask:
            def __init__(self, config):
                pass
            def run(self):
                return {"status": "success"}

        self.manager.register_task('dummy_task', DummyTask)
        result = self.manager.execute_task('dummy_task')
        self.assertIsInstance(result, dict)
        self.assertIn('status', result)
        self.assertEqual(result['status'], 'success')

if __name__ == '__main__':
    unittest.main()
