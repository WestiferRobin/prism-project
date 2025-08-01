from typing import List

from src.api.builders.config_builders.drone_configs import build_drone_config
from src.api.builders.model_builders.prism_builders.avatar_builder import build_avatar_drone
from src.api.converters.date_converter import convert_to_date
from src.api.helpers.app_helper import configure_apps
from src.utils.configs.app_configs import AppConfig
from src.utils.configs.model_configs.prism_config import PrismConfig
from src.utils.configs.model_configs.user_config import UserConfig
from src.utils.constants.user_constants import WES_ID, EMMA_ID, MARY_ID, MAX_ID, TYLER_ID, PAYTON_ID, BRIAN_ID
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
    payton_avatar = build_avatar_drone(config=payton_config)
    payton_apps = configure_apps(version=version, user_id=payton_config.user_id)

    return build_user_config(
        avatar_config=payton_avatar.config.avatar_config,
        app_configs=[app.config for app in payton_apps],
    )


def build_brian_config(version: int) -> UserConfig:
    brian_config = build_drone_config(
        version=version,
        name="Brian Psi",
        alias="brian-psi",
        dna=BRIAN_ID,
        age=AgeType.Adult,
        gender=GenderType.Male,
        race=RaceType.Human,
        rank=RankType.Arch,
        date=convert_to_date(month=11, day=28, year=1979)
    )
    brian_avatar = build_avatar_drone(config=brian_config)
    brian_apps = configure_apps(version=version, user_id=brian_config.user_id)

    return build_user_config(
        avatar_config=brian_avatar.config.avatar_config,
        app_configs=[app.config for app in brian_apps],
    )

