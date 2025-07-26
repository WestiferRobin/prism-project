from typing import List

from pydantic import BaseModel

from src.app import App
from src.app.bot import Bot
from src.app.game import Game
from src.app.tools import Tool
from src.models.prisms import Prism


class PrismNet(BaseModel):
    version: int

    apps: List[App]
    bots: List[Bot]

    def __str__(self):
        return f"Prism.net: version {self.version}"

    @property
    def games(self) -> List[Game]:
        game_list = list(filter(lambda app : isinstance(app, Game), self.apps))
        return game_list

    @property
    def tools(self) -> List[Tool]:
        tool_list = list(filter(lambda app : isinstance(app, Tool), self.apps))
        return tool_list

    @property
    def prisms(self) -> List[Prism]:
        prisms = []

        for app in self.apps:
            app_drones = app.drones
            for app_drone in app_drones:
                prisms.append(app_drone.prism)

        for tool in self.tools:
            tool_drones = tool.drones
            for tool_drone in tool_drones:
                prisms.append(tool_drone.prism)

        return prisms

