from abc import ABC
from autospark_kit.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List

from api_client_tool import APIClientTool


class IflytekArtifactoryToolkit(BaseToolkit, ABC):
    name: str = "api client tools"
    description: str = "api client tools provides generic interaction for invoking external generic apis"

    def get_tools(self) -> List[BaseTool]:
        return [APIClientTool()]

    def get_env_keys(self) -> List[str]:
        return ["URL"]

