from src.api.builders.config_builders.drone_configs import build_drone_config
from src.api.builders.config_builders.drone_configs.celeberty_configs import build_gordon_config
from src.api.builders.config_builders.user_configs import build_user_config
from src.api.converters.date_converter import convert_to_date
from src.api.helpers.app_helper import configure_apps
from src.utils.configs.model_configs.user_config import UserConfig
from src.utils.constants.user_constants import MARY_ID
from src.utils.enums.prism_enums import AgeType, GenderType, RaceType, RankType


def build_mary_config(version: int) -> UserConfig:
    mary_config = build_drone_config(
        version=version,
        name="Mary Lambda",
        alias="mary-lambda",
        dna=MARY_ID,
        age=AgeType.Adult,
        gender=GenderType.Female,
        race=RaceType.Human,
        rank=RankType.Arch,
        date=convert_to_date(month=8, day=18, year=1969)
    )
    companion_config = build_gordon_config(version=version)
    mary_apps = configure_apps(version=version, user_id=mary_config.id)

    return build_user_config(
        avatar_config=mary_config,
        companion_config=companion_config,
        app_configs=[app.config for app in mary_apps],
    )

