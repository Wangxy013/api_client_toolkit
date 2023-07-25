import json
import unittest

from api_client_tool import APIClientTool, ApiClientInput


class ToolTestCase(unittest.TestCase):
    def setUp(self):
        self.tool = APIClientTool()

    def test_tool_name(self):
        self.assertEqual(self.tool.name, "API Client Tool")

    def test_tool_args_schema(self):
        self.assertEqual(self.tool.args_schema, ApiClientInput)

    def test_tool_description(self):
        self.assertEqual(self.tool.description, "Request the external api interface to get the result")

    def test_execute_method(self):
        apiclient_input = ApiClientInput(parameters="name=iflytek")
        expected_output = "abc"
        output = self.tool._execute(parameters=apiclient_input.parameters)
        # 判空，解析json，取出json中的data字符串
        data = self.text_to_json(output).get("data")
        self.assertEqual(data, expected_output)

    def text_to_json(self,text):
        jsonObj = json.loads(text)
        return jsonObj