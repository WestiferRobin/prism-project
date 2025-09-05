from src.api.builders.app_builders import build_prism_hive
from src.api.builders.app_builders.game_builder import build_solar_conquest, build_game
from src.api.builders.app_builders.studio_builder import build_prism_studio, build_prism_forge, build_prism_lab
from src.api.validators.app_validators import validate_studio, validate_hive, validate_lab, validate_forge
from src.api.validators.app_validators.game_validator import validate_game
from src.models.app.forge import Forge
from src.models.app.game import Game
from src.models.app.lab import Lab
from src.models.app.studio import Studio
from src.utils.constants import DEBUG_VERSION, DEV_VERSION, TEST_VERSION, PROD_VERSION, FINAL_VERSION


def test_game(game: Game = None, version: int = DEBUG_VERSION):
    if game is None:
        game = build_solar_conquest(version=version)
    validate_game(
        source_game=game,
        target_game=build_game(config=game.game_config),
    )


def test_studio(studio: Studio = None, version: int = DEV_VERSION):
    if studio in None:
        studio = build_prism_studio(version=version)
    validate_studio(
        source_studio=studio,
        target_studio=build_studio(config=studio.studio_config)
    )


def test_hive(hive: Hive = None, version: int = TEST_VERSION):
    if hive is None:
        hive = build_prism_hive(version=version)
    validate_hive(
        source_hive=hive,
        target_hive=build_hive(config=hive.hive_config)
    )


def test_lab(lab: Lab = None, version: int = PROD_VERSION):
    if lab is None:
        lab = build_prism_lab(version=version)
    validate_lab(
        source_lab=lab,
        target_lab=build_lab(config=lab.lab_config)
    )


def test_forge(forge: Forge = None, version: int = FINAL_VERSION):
    if forge is None:
        forge = build_prism_forge(version=version)
    validate_forge(
        source_forge=forge,
        target_forge=build_forge(config=forge.forge_config)
    )

