from uuid import UUID

from src.api.builders import build_server_config
from src.api.builders.config_builders.bot_configs import build_bot_config, build_speeder_config
from src.api.helpers.alias_helper import create_alias
from src.models.drones.bot_drone import BotDrone
from src.models.bots.hedron_server import HedronServer
from src.models.vehicles.speeders.bot_speeder import BotSpeeder
from src.utils.configs.model_configs.drone_config import DroneConfig
from src.utils.configs.model_configs.user_config import UserConfig


def build_hedron_server(
    version: int,
    owner_config: UserConfig,
    companion_config: DroneConfig,
    server_name: str = "Hedron Server",
    server_alias: str = "hedron-server",
) -> HedronServer:
    server_config = build_server_config(
        version=version,
        server_name=server_name,
        server_alias=server_alias,
        owner_config=owner_config,
        companion_config=companion_config,
    )
    return HedronServer(config=server_config)


def build_bot_drone(
    version: int,
    bot_name: str,
    bot_alias: str,
    owner_id: UUID
) -> BotDrone:
    bot_config = build_bot_config(
        version=version,
        bot_name=bot_name,
        bot_alias=bot_alias,
        owner_id=owner_id
    )
    return BotDrone(config=bot_config)


def build_bot_speeder(version: int, owner_id: UUID, pilot_name: str) -> BotSpeeder:
    pilot_config = build_bot_config(
        version=version,
        bot_name=pilot_name,
        bot_alias=create_alias(name=pilot_name),
        owner_id=owner_id
    )
    speeder_config = build_speeder_config(pilot_config=pilot_config)
    return BotSpeeder(config=speeder_config)


def build_bot_legion(
    version: int,
    owner_config: UserConfig,
    legion_name: str = "Bot Legion",
    legion_alias: str = "bot-legion",
):
    legion_config = build_legion_config()
    return BotLegion(config=legion_config)



