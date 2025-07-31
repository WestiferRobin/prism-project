from typing import List, Dict, cast
from uuid import UUID

from pydantic import BaseModel

from src.api.builders.app_builders import build_app
from src.app import App
from src.app.game import Game
from src.app.tools import Tool
from src.app.widgets import Widget
from src.models.drones import Drone
from src.models.drones.bot_drone import BotDrone
from src.models.hedron_server import HedronServer
from src.models.legion.bot_legion import BotLegion
from src.models.vehicles.speeders.bot_speeder import BotSpeeder
from src.utils.configs.app_configs.game_config import GameConfig
from src.utils.configs.app_configs.tool_config import ToolConfig
from src.utils.configs.app_configs.widget_config import WidgetConfig
from src.utils.configs.net_config import NetConfig
from src.utils.user import User


class PrismNet(BaseModel):
    config: NetConfig

    hedron: HedronServer
    speeder: BotSpeeder
    legion: BotLegion

    def __init__(self, **net_data):
        super().__init__(**net_data)

    def __str__(self):
        return f"Prism.net: version {self.version}"

    @property
    def users(self) -> List[User]:
        users = []
        for user_config in self.config.user_configs:
            user = User(config=user_config)
            users.append(user)
        return users

    @property
    def apps(self) -> List[App]:
        apps = []
        for app_config in self.config.app_configs:
            app = App(config=app_config)
            apps.append(app)
        return apps

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
    def tools(self) -> List[Tool]:
        tools = []
        for app_config in self.config.app_configs:
            if isinstance(app_config, ToolConfig):
                tool_config = cast(ToolConfig, app_config)
                tool = Tool(config=tool_config)
                tools.append(tool)
        return tools

    @property
    def widgets(self) -> List[Widget]:
        widgets = []
        for app_config in self.config.app_configs:
            if isinstance(app_config, WidgetConfig):
                widget_config = cast(WidgetConfig, app_config)
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

