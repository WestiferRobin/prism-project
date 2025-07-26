from typing import List

from pydantic import BaseModel

from src.app import App
from src.app.game import Game
from src.app.tools import Tool
from src.models.drones.bot_drone import BotDrone
from src.models.hive_server import HiveServer
from src.models.legion import Legion
from src.models.prisms import Prism


class PrismNet(BaseModel):
    version: int
    name: str = "Prism.net"

    apps: List[App]
    server: HiveServer
    bot: BotDrone
    avatar_legion: Legion

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

        for prism_app in self.apps:
            app_drones = prism_app.drones
            for app_drone in app_drones:
                prisms.append(app_drone.prism)

        for drone in self.server.drones:
            prisms.append(drone.prism)

        prisms.append(self.bot.prism)

        for drone in self.avatar_legion.drones:
            prisms.append(drone.prism)

        return prisms

