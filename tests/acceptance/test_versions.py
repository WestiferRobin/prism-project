from src.api.builders.mvp_builder import build_mvp
from src.api.builders.net_builder import build_prism_net
from src.api.services.app_service import get_apps
from src.api.services.bot_service import get_bots
from src.api.services.user_service import get_users
from src.api.validators import validate_mvp
from src.utils.constants import (
    DEV_VERSION,
    TEST_VERSION,
    PROD_VERSION,
    ALPHA_VERSION,
    BETA_VERSION,
    FINAL_VERSION,
    DEBUG_VERSION
)


def test_dev_mvp():
    mvp_version = DEV_VERSION

    users = get_users(version=mvp_version)
    user_configs = [user.config for user in users]

    mvp = build_mvp(
        version=mvp_version,
        user_configs=user_configs
    )
    prism_net = build_prism_net(
        version=mvp_version,
        users=users,
        apps=get_apps(
            version=mvp_version,
            user_configs=user_configs
        ),
        bots=get_bots(
            version=mvp_version,
            user_configs=user_configs
        )
    )
    validate_mvp(
        source_mvp=mvp,
        target_mvp=prism_net,
    )


def test_test_mvp():
    mvp_version = TEST_VERSION

    users = get_users(version=mvp_version)
    user_configs = [user.config for user in users]

    mvp = build_mvp(
        version=mvp_version,
        user_configs=user_configs
    )
    prism_net = build_prism_net(
        version=mvp_version,
        users=users,
        apps=get_apps(
            version=mvp_version,
            user_configs=user_configs
        ),
        bots=get_bots(
            version=mvp_version,
            user_configs=user_configs
        )
    )
    validate_mvp(
        source_mvp=mvp,
        target_mvp=prism_net,
    )


def test_prod_mvp():
    mvp_version = PROD_VERSION

    users = get_users(version=mvp_version)
    user_configs = [user.config for user in users]

    mvp = build_mvp(
        version=mvp_version,
        user_configs=user_configs
    )
    prism_net = build_prism_net(
        version=mvp_version,
        users=users,
        apps=get_apps(
            version=mvp_version,
            user_configs=user_configs
        ),
        bots=get_bots(
            version=mvp_version,
            user_configs=user_configs
        )
    )
    validate_mvp(
        source_mvp=mvp,
        target_mvp=prism_net,
    )


def test_alpha_mvp():
    mvp_version = ALPHA_VERSION

    users = get_users(version=mvp_version)
    user_configs = [user.config for user in users]

    mvp = build_mvp(
        version=mvp_version,
        user_configs=user_configs
    )
    prism_net = build_prism_net(
        version=mvp_version,
        users=users,
        apps=get_apps(
            version=mvp_version,
            user_configs=user_configs
        ),
        bots=get_bots(
            version=mvp_version,
            user_configs=user_configs
        )
    )
    validate_mvp(
        source_mvp=mvp,
        target_mvp=prism_net,
    )


def test_beta_mvp():
    mvp_version = BETA_VERSION

    users = get_users(version=mvp_version)
    user_configs = [user.config for user in users]

    mvp = build_mvp(
        version=mvp_version,
        user_configs=user_configs
    )
    prism_net = build_prism_net(
        version=mvp_version,
        users=users,
        apps=get_apps(
            version=mvp_version,
            user_configs=user_configs
        ),
        bots=get_bots(
            version=mvp_version,
            user_configs=user_configs
        )
    )
    validate_mvp(
        source_mvp=mvp,
        target_mvp=prism_net,
    )


def test_final_mvp():
    mvp_version = FINAL_VERSION

    users = get_users(version=mvp_version)
    user_configs = [user.config for user in users]

    mvp = build_mvp(
        version=mvp_version,
        user_configs=user_configs
    )
    prism_net = build_prism_net(
        version=mvp_version,
        users=users,
        apps=get_apps(
            version=mvp_version,
            user_configs=user_configs
        ),
        bots=get_bots(
            version=mvp_version,
            user_configs=user_configs
        )
    )
    validate_mvp(
        source_mvp=mvp,
        target_mvp=prism_net,
    )


def test_debug_mvp():
    mvp_version = DEBUG_VERSION

    users = get_users(version=mvp_version)
    user_configs = [user.config for user in users]

    mvp = build_mvp(
        version=mvp_version,
        user_configs=user_configs
    )
    prism_net = build_prism_net(
        version=mvp_version,
        users=users,
        apps=get_apps(
            version=mvp_version,
            user_configs=user_configs
        ),
        bots=get_bots(
            version=mvp_version,
            user_configs=user_configs
        )
    )
    validate_mvp(
        source_mvp=mvp,
        target_mvp=prism_net,
    )

