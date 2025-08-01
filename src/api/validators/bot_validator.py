from src.api import build_user
from src.api.validators.config_validators.bot_configs import validate_bot_config
from src.api.validators.config_validators.server_configs import validate_server_config
from src.models.drones.bot_drone import BotDrone
from src.bots import HedronServer


def validate_server(server: HedronServer, expected_value: HedronServer) -> None:
    assert server is not None
    assert expected_value is not None
    assert isinstance(server, HedronServer)

    assert server.id == expected_value.id
    validate_server_config(config=server.config, expected_value=expected_value.config)

    owner = server.owner
    owner_config = build_user_config(,
    valid_user = build_user(config=owner_config)
    validate_user(user=owner, expected_value=valid_user)


def validate_bot(bot: BotDrone, expected_value: BotDrone) -> None:
    assert bot is not None
    assert expected_value is not None

    validate_bot_config(config=bot.bot_config, expected_value=expected_value.bot_config)
