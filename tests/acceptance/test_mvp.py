from src.api.builders.model_builders.user_builder import build_users
from src.api.builders.mvp_builder import build_mvp
from src.api.builders.net_builder import build_prism_net
from src.api.services.app_service import get_apps
from src.api.services.bot_service import get_bots
from src.api.services.user_service import get_user_configs
from src.api.validators import validate_mvp
from src.utils.constants import MVP_VERSIONS


def test_mvp():
    for mvp_version in MVP_VERSIONS:
        user_configs = get_user_configs(version=mvp_version)
        mvp = build_mvp(
            version=mvp_version,
            user_configs=user_configs
        )

        prism_net = build_prism_net(
            version=mvp_version,
            users=build_users(configs=user_configs),
            apps=get_apps(
                version=mvp_version,
                user_configs=user_configs
            ),
            bots=get_bots(
                version=mvp_version,
                user_configs=user_configs
            )
        )

        validate_mvp(source_mvp=mvp, target_mvp=prism_net)

