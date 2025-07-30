from typing import List, Dict
from uuid import UUID

from pydantic import BaseModel

from src.app import App
from src.app.game import Game
from src.app.tools import Tool
from src.app.widgets import Widget
from src.models.drones import Drone
from src.models.drones.bot_drone import BotDrone
from src.models.hedron_server import HedronServer
from src.models.legion.bot_legion import BotLegion
from src.utils.configs.net_config import NetConfig


class PrismNet(BaseModel):
    config: NetConfig

    apps: List[App] = []
    hedron: HedronServer
    speeder: BotDrone
    legion: BotLegion

    def __init__(self, **net_data):
        super().__init__(**net_data)

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
    def widgets(self) -> List[Widget]:
        widget_list = list(filter(lambda app : isinstance(app, Widget), self.apps))
        return widget_list

    @property
    def drones(self) -> List[Drone]:
        drone_list = []
        for app in self.apps:
            for drone in app.drones:
                drone_list.append(drone)
        return drone_list

    @property
    def registry(self) -> Dict[UUID, Drone]:
        drones = self.drones
        registry = { drone.id: drone for drone in drones }
        return registry

