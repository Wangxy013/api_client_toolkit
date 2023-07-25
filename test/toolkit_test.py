import unittest

from api_client_tool import APIClientTool
from api_client_toolkit import ApiClientToolkit


class ToolkitTests(unittest.TestCase):
    def setUp(self):
        self.toolkit = ApiClientToolkit()

    def test_get_tools_returns_list_of_tools(self):
        tools = self.toolkit.get_tools()
        self.assertIsInstance(tools, list)
        self.assertTrue(all(isinstance(tool, APIClientTool) for tool in tools))

    def test_get_env_keys_returns_list_of_strings(self):
        env_keys = self.toolkit.get_env_keys()
        self.assertIsInstance(env_keys, list)
        self.assertTrue(all(isinstance(key, str) for key in env_keys))

    def test_toolkit_has_name_and_description(self):
        self.assertEqual(self.toolkit.name, "api client toolkit")
        self.assertEqual(self.toolkit.description, "api client toolkit provides generic interaction for invoking external generic apis")
