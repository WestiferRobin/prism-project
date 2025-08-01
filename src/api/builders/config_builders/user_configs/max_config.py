from src.api.builders.config_builders.account_configs import build_account_config
from src.api.builders.config_builders.drone_configs import build_drone_config
from src.api.builders.config_builders.drone_configs.celeberty_configs import build_harrison_config
from src.api.builders.config_builders.user_configs import build_user_config
from src.api.converters.date_converter import convert_to_date
from src.api.helpers.app_helper import configure_apps
from src.utils.configs.model_configs.user_config import UserConfig
from src.utils.constants.user_constants import MAX_ID
from src.utils.enums.prism_enums import AgeType, GenderType, RaceType, RankType


def build_max_config(version: int) -> UserConfig:
    max_config = build_drone_config(
        version=version,
        name="Max Alpha",
        alias="max-alpha",
        dna=MAX_ID,
        age=AgeType.Adult,
        gender=GenderType.Male,
        race=RaceType.Human,
        rank=RankType.Arch,
        date=convert_to_date(month=2, day=19, year=1993)
    )
    companion_config = build_harrison_config(version=version)
    account_configs = []
    max_apps = configure_apps(version=version, user_id=max_config.id)
    for app in max_apps:
        account_config = build_account_config(
            version=version,
            user_id=max_config.id,
            app_name=app.config.name,
            app_alias=app.config.alias,
        )
        account_configs.append(account_config)

    return build_user_config(
        avatar_config=max_config,
        companion_config=companion_config,
        account_configs=account_configs
    )

