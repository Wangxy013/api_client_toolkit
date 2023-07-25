from abc import ABC
from typing import Type, List

from superagi.tools.base_tool import BaseToolkit, BaseTool

from api_client_tool import APIClientTool


class ApiClientToolkit(BaseToolkit, ABC):
    name: str = "API Client ToolKit"
    description: str = "Api client toolkit provides generic interaction for invoking external generic apis"

    def get_tools(self) -> List[BaseTool]:
        return [APIClientTool()]

    def get_env_keys(self) -> List[str]:
        return ["URL"]

