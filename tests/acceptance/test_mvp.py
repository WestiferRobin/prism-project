from src.api import build_user
from src.api.builders import build_mvp
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

        users = []
        for user_config in user_configs:
            user = build_user(config=user_config)
            users.append(user)

        validate_mvp(
            version=mvp_version,
            mvp=mvp,
            users=users
        )

