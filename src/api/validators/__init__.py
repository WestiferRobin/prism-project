from typing import List

from src.api.validators.bot_validator import validate_bot_drone
from src.api.validators.legion_validator import validate_legion
from src.api.validators.server_validator import validate_hive_server
from src.models.legion import Legion
from src.models.drones.bot_drone import BotDrone
from src.models.hive_server import HiveServer
from src.api.validators.app_validators import validate_app
from src.api.validators.app_validators.game_validator import validate_game
from src.api.validators.app_validators.tool_validator import validate_tool
from src.api.validators.drone_validator import validate_drone
from src.app import App
from src.app.game import Game
from src.app.tools import Tool
from src.prism_net import PrismNet


def validate_mvp_games(games: List[Game]):
    assert len(games) > 0

    for game in games:
        validate_game(game)


def validate_mvp_tools(tools: List[Tool]):
    assert len(tools) > 0

    for tool in tools:
        validate_tool(tool)


def validate_mvp_apps(apps: List[App]):
    assert len(apps) > 0

    for app in apps:
        validate_app(app)

    games = list(filter(lambda g: isinstance(g, Game), apps))
    validate_mvp_games(games)

    tools = list(filter(lambda g: isinstance(g, Tool), apps))
    validate_mvp_tools(tools)


def validate_mvp_server(server: HiveServer):
    validate_hive_server(server=server)


def validate_mvp_bot(bot: BotDrone):
    validate_bot_drone(bot=bot)


def validate_mvp_legion(avatar_legion: Legion):
    validate_legion(legion=avatar_legion)


def validate_mvp(mvp: PrismNet):
    assert isinstance(mvp, PrismNet)
    assert mvp.name is not None
    assert isinstance(mvp.name, str)

    validate_mvp_apps(apps=mvp.apps)
    validate_mvp_server(server=mvp.server)
    validate_mvp_bot(bot=mvp.bot)
    validate_mvp_legion(avatar_legion=mvp.avatar_legion)

