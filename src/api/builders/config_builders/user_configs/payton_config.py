from src.api.builders.config_builders.account_configs import build_account_config
from src.api.builders.config_builders.drone_configs import build_drone_config, build_jeffery_config
from src.api.builders.config_builders.user_configs import build_user_config
from src.api.converters.date_converter import convert_to_date
from src.api.helpers.app_helper import configure_apps
from src.utils.configs.model_configs.user_config import UserConfig
from src.utils.constants.user_constants import PAYTON_ID
from src.utils.enums.prism_enums import AgeType, GenderType, RaceType, RankType

def build_payton_config(version: int) -> UserConfig:
    payton_config = build_drone_config(
        version=version,
        name="Payton Sigma",
        alias="payton-sigma",
        dna=PAYTON_ID,
        age=AgeType.Adult,
        gender=GenderType.Male,
        race=RaceType.Human,
        rank=RankType.Arch,
        date=convert_to_date(month=5, day=16, year=2000)
    )
    companion_config = build_jeffery_config(version=version)
    account_configs = []
    payton_apps = configure_apps(version=version, user_id=payton_config.id)
    for app in payton_apps:
        account_config = build_account_config(
            version=version,
            user_id=payton_config.id,
            app_name=app.config.name,
            app_alias=app.config.alias,
        )
        account_configs.append(account_config)

    return build_user_config(
        avatar_config=payton_config,
        companion_config=companion_config,
        account_configs=account_configs
    )
