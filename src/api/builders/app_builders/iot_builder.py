from src.api.builders.model_builders.bot_builder import build_bot_drone
from src.api.builders.config_builders.bot_configs import build_server_config, build_bot_config
from src.api.builders.model_builders.legion_builder import build_legion
from src.api.builders.model_builders.prism_builders.avatar_builder import build_avatar_legion_drone
from src.models.drones.bot_drone import BotDrone
from src.models.hive_server import HedronServer
from src.models.legion import Legion
from src.utils.configs.model_configs.user_config import UserConfig
from src.utils.enums.prism_enums import RankType


def build_hedron_hive(version: int) -> HedronServer:
    server_config = build_server_config(version=version, name="Hedron Hive")
    hedron_hive = HedronServer(config=server_config)
    return hedron_hive


def build_hedron_bot(version: int) -> BotDrone:
    bot_config = build_bot_config(name="Hedron Bot", version=version)
    bot_drone = build_bot_drone(config=bot_config)
    return bot_drone


def build_avatar_legion(version: int, avatar_config: UserConfig) -> Legion:
    avatar_config.rank = RankType.Arch
    avatar = build_avatar_legion_drone(config=avatar_config)
    avatar_legion = build_legion(version=version, admin=avatar)
    return avatar_legion

