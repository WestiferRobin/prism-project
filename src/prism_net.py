from typing import List, Dict, cast
from uuid import UUID

from pydantic import BaseModel

from src.app import App
from src.app.game import Game
from src.app.lab import Lab
from src.app.widget import Widget
from src.bots import Bot
from src.models.drones import Drone
from src.utils.configs.app_configs.game_config import GameConfig
from src.utils.configs.app_configs.lab_config import LabConfig
from src.utils.configs.app_configs.forge_config import ForgeConfig
from src.utils.configs.net_config import NetConfig
from src.utils.user import User


class PrismNet(BaseModel):
    config: NetConfig

    users: List[User]
    drones: List[Drone]

    apps: List[App]
    bots: List[Bot]

    def __init__(self, **net_data):
        super().__init__(**net_data)


    @property
    def games(self) -> List[Game]:
        games = []
        for app_config in self.config.app_configs:
            if isinstance(app_config, GameConfig):
                game_config = cast(GameConfig, app_config)
                game = Game(config=game_config)
                games.append(game)
        return games

    @property
    def tools(self) -> List[Lab]:
        tools = []
        for app_config in self.config.app_configs:
            if isinstance(app_config, LabConfig):
                tool_config = cast(LabConfig, app_config)
                tool = Lab(config=tool_config)
                tools.append(tool)
        return tools

    @property
    def widgets(self) -> List[Widget]:
        widgets = []
        for app_config in self.config.app_configs:
            if isinstance(app_config, ForgeConfig):
                widget_config = cast(ForgeConfig, app_config)
                widget = Widget(config=widget_config)
                widgets.append(widget)
        return widgets

    @property
    def drones(self) -> List[Drone]:
        drone_list = []
        for app in self.apps:
            for drone in app.drones:
                drone_list.append(drone)
        return drone_list

    @property
    def registry(self) -> Dict[UUID, Drone]:
        registry = { }
        for user in self.users:
            registry[user.id] = user.avatar
        for app in self.apps:
            for drone in app.drones:
                registry[drone.id] = drone
        return registry

