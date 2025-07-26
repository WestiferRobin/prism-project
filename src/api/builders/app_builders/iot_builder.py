from src.api.builders.bot_builder import build_bot_drone
from src.api.builders.config_builders.bot_configs import build_server_config, build_bot_config
from src.api.builders.legion_builder import build_legion
from src.api.builders.prism_builders.avatar_builder import build_avatar
from src.models.drones.bot_drone import BotDrone
from src.models.hive_server import HiveServer
from src.models.legion import Legion
from src.utils.configs.user_config import UserConfig


def build_hedron_hive(version: int = 0) -> HiveServer:
    server_config = build_server_config(version=version, name="Hedron Hive")
    hedron_hive = HiveServer(config=server_config)
    return hedron_hive


def build_hedron_bot(version: int = 0) -> BotDrone:
    bot_config = build_bot_config(name="Hedron Bot", version=version)
    bot_drone = build_bot_drone(config=bot_config)
    return bot_drone


def build_avatar_legion(avatar_config: UserConfig) -> Legion:
    avatar = build_avatar(config=avatar_config)
    avatar_legion = build_legion(admin=avatar)
    return avatar_legion

