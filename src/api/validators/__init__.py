from typing import List

from src import PrismNet
from src.api.validators.app_validators import validate_app
from src.api.validators.app_validators.game_validator import validate_game
from src.api.validators.app_validators.tool_validator import validate_tool
from src.api.validators.drone_validator import validate_drone
from src.app import App
from src.app.bot import Bot
from src.app.game import Game
from src.app.tools import Tool


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


def validate_mvp_bots(bots: List[Bot]):
    assert len(bots) > 0

    for bot in bots:
        validate_drone(bot.drone)


def validate_mvp(mvp: PrismNet):
    assert isinstance(mvp, PrismNet)
    assert mvp.name is not None
    assert isinstance(mvp.name, str)

    validate_mvp_apps(mvp.apps)
    validate_mvp_bots(mvp.bots)

