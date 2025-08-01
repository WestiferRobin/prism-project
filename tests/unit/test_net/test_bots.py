from src.api.builders import build_hedron_hive
from src.api.builders.model_builders.bot_builder import build_bot_drone
from src.api.validators import validate_server, validate_bot
from src.utils.constants import DEV_VERSION


def test_hedron_server(version: int = DEV_VERSION) -> None:
    hedron_server = build_hedron_hive(version=version)
    validate_server(server=hedron_server, version=version)


def test_bot_drone(version: int = DEV_VERSION) -> None:
    bot_drone = build_bot_drone(version=version)
    validate_bot(bot=bot_drone, version=version)


def test_bot_speeder(version: int = DEV_VERSION) -> None:
    bot_speeder = build_bot_speeder(version=version)
    validate_speeder(bot=bot_speeder, version=version)


def test_bot_legion(version: int = DEV_VERSION) -> None:
    bot_legion = build_bot_legion(version=version)
    validate_legion(legion=bot_legion, version=version)

