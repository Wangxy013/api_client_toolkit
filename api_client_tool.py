from typing import Type

import requests
from pydantic import BaseModel, Field
from superagi.tools.base_tool import BaseTool


def get(url):
    response = requests.get(url, headers=None)
    return response.text


def post(url, data):
    response = requests.post(url, headers=None, json=data)
    return response.text


class ApiClientInput(BaseModel):
    parameters: str = Field(..., description="Function parameters of the url request")


class APIClientTool(BaseTool):
    """
    APIClientTool
    """
    name: str = "API Client Tool"
    args_schema: Type[BaseModel] = ApiClientInput
    description: str = "Request the external api interface to get the result"

    def _execute(self, parameters: str = None):
        url = self.get_tool_config('URL')+"?"+parameters
        print("url="+url)
        return get(url)
