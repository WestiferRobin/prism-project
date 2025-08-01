from src.api.builders.config_builders.drone_configs import build_drone_config
from src.api.builders.config_builders.drone_configs.celeberty_configs import build_patrick_config
from src.api.builders.config_builders.user_configs import build_user_config
from src.api.converters.date_converter import convert_to_date
from src.api.helpers.app_helper import configure_apps
from src.utils.configs.model_configs.user_config import UserConfig
from src.utils.constants.user_constants import TYLER_ID
from src.utils.enums.prism_enums import AgeType, GenderType, RaceType, RankType


def build_tyler_config(version: int) -> UserConfig:
    tyler_config = build_drone_config(
        version=version,
        name="Tyler Gamma",
        alias="tyler-gamma",
        dna=TYLER_ID,
        age=AgeType.Adult,
        gender=GenderType.Male,
        race=RaceType.Human,
        rank=RankType.Arch,
        date=convert_to_date(month=3, day=6, year=1996)
    )
    companion_config = build_patrick_config(version=version)
    tyler_apps = configure_apps(version=version, user_id=tyler_config.id)

    return build_user_config(
        avatar_config=tyler_config,
        companion_config=companion_config,
        app_configs=[app.config for app in tyler_apps],
    )