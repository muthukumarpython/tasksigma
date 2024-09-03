# tasksigma/src/tests/test_react.py

import unittest
from react.react_agent import ReActAgent
from react.react_utils import process_environment, format_reasoning

class TestReActAgent(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment for ReActAgent tests.
        """
        self.config = {
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
        }
        self.agent = ReActAgent(self.config)

    def test_reason(self):
        """
        Test the reasoning capability of the ReActAgent.
        """
        prompt = "How can we optimize our workflow?"
        reasoning_trace = self.agent.reason(prompt)
        self.assertIsInstance(reasoning_trace, str)
        self.assertIn("This is a simulated response from the model.", reasoning_trace)

    def test_act(self):
        """
        Test the action-taking capability of the ReActAgent.
        """
        action = "Query the database for recent metrics."
        result = self.agent.act(action)
        self.assertIsInstance(result, dict)
        self.assertIn("error", result)  # Expecting an error since the endpoint is a placeholder

    def test_run(self):
        """
        Test the full reasoning and acting cycle of the ReActAgent.
        """
        prompt = "How do we increase team productivity?"
        result = self.agent.run(prompt)
        self.assertIsInstance(result, dict)
        self.assertIn("reasoning", result)
        self.assertIn("result", result)

class TestReActUtils(unittest.TestCase):
    def test_process_environment(self):
        """
        Test the process_environment utility function.
        """
        environment_data = {
            "metric1": "value1",
            "metric2": "value2"
        }
        processed_data = process_environment(environment_data)
        self.assertEqual(processed_data, "Processed data: metric1: value1, metric2: value2")

    def test_format_reasoning(self):
        """
        Test the format_reasoning utility function.
        """
        reasoning_trace = " This is a sample reasoning trace. "
        formatted_trace = format_reasoning(reasoning_trace)
        self.assertEqual(formatted_trace, "Reasoned: This is a sample reasoning trace.")

if __name__ == '__main__':
    unittest.main()
