from src.api.builders.config_builders import build_net_config
from src.api.validators.bot_validator import validate_bot
from src.api.validators.model_validators.bot_validator import validate_bot_drone
from src.api.validators.config_validators import validate_config
from src.api.validators.model_validators.legion_validator import validate_legion
from src.api.validators.model_validators.server_validator import validate_server
from src.api.validators.app_validators import validate_app
from src.api.validators.app_validators.game_validator import validate_game
from src.api.validators.app_validators.tool_validator import validate_tool
from src.api.validators.model_validators.drone_validator import validate_drone
from src.prism_net import PrismNet


def validate_mvp(mvp: PrismNet, expected_version: int):
    assert isinstance(mvp, PrismNet)

    expected_value = build_net_config(version=expected_version)
    validate_config(
        config=mvp.config,
        expected_value=expected_value,
    )

    for app in mvp.apps:
        validate_app(app=app, expected_platform=app.platform)


