from typing import List

from src.prism_net import Mvp


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

    games = filter(lambda g: isinstance(g, Game), apps)
    validate_mvp_games(games)

    tools = filter(lambda g: isinstance(g, Tool), apps)
    validate_mvp_tools(tools)


def validate_mvp_bots(bots: List[Bot]):
    assert len(bots) > 0

    for bot in bots:
        validate_drone(bot.drone)


def validate_mvp(mvp: Mvp):
    assert isinstance(mvp, Mvp)
    assert mvp.name is not None

    validate_apps(mvp.apps)
    validate_bots(mvp.bots)
