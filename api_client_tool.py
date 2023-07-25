from typing import Type

import requests
from autospark_kit.tools.base_tool import BaseTool
from pydantic import BaseModel, Field


def get(url):
    response = requests.get(url, headers=None)
    return response


def post(url, data):
    response = requests.post(url, headers=None, json=data)
    return response


class ListImageTagsInput(BaseModel):
    url: str = Field(..., description="url of the external api interface")


class APIClientTool(BaseTool):
    """
    APIClientTool
    """
    name: str = "API Client Tool"
    args_schema: Type[BaseModel] = ListImageTagsInput
    description: str = "Request the external api interface to get the result"

    def _execute(self, repo_path: str = None):
        url = self.get_tool_config('URL')
        return get(url)
