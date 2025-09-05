from test_apps import test_game, test_studio, test_hive, test_lab, test_forge
from src.api.builders.company_builder import build_company
from src.api.builders.mvp_builder import build_mvp
from src.utils.constants import DEBUG_VERSION, DEV_VERSION, TEST_VERSION, PROD_VERSION, FINAL_VERSION
from src.api.validators.company_validator import validate_company


def test_debug_version():
    prism_co = build_mvp(version=DEBUG_VERSION)
    validate_company(
        source_company=prism_co,
        target_company=build_company(
            version=prism_co.config.version,
            company_name=prism_co.config.name,
            leader_config=prism_co.config.leader_config
        )
    )
    test_game(game=prism_co.game, version=prism_co.version)


def test_dev_version():
    prism_co = build_mvp(version=DEV_VERSION)
    validate_company(
        source_company=prism_co,
        target_company=build_company(
            version=prism_co.config.version,
            company_name=prism_co.config.name,
            leader_config=prism_co.config.leader_config
        )
    )
    test_game(game=prism_co.game, version=prism_co.version)
    test_studio(studio=prism_co.studio, version=prism_co.version)


def test_test_version():
    prism_co = build_mvp(version=TEST_VERSION)
    validate_company(
        source_company=prism_co,
        target_company=build_company(
            version=prism_co.config.version,
            company_name=prism_co.config.name,
            leader_config=prism_co.config.leader_config
        )
    )
    test_game(game=prism_co.game, version=prism_co.version)
    test_studio(studio=prism_co.studio, version=prism_co.version)
    test_hive(hive=prism_co.hive, version=prism_co.version)


def test_prod_version():
    prism_co = build_mvp(version=PROD_VERSION)
    validate_company(
        source_company=prism_co,
        target_company=build_company(
            version=prism_co.config.version,
            company_name=prism_co.config.name,
            leader_config=prism_co.config.leader_config
        )
    )
    test_game(game=prism_co.game, version=prism_co.version)
    test_studio(studio=prism_co.studio, version=prism_co.version)
    test_hive(hive=prism_co.hive, version=prism_co.version)
    test_lab(lab=prism_co.lab, version=prism_co.version)


def test_final_version():
    prism_co = build_mvp(version=FINAL_VERSION)
    validate_company(
        source_company=prism_co,
        target_company=build_company(
            version=prism_co.config.version,
            company_name=prism_co.config.name,
            leader_config=prism_co.config.leader_config
        )
    )
    test_game(game=prism_co.game, version=prism_co.version)
    test_studio(studio=prism_co.studio, version=prism_co.version)
    test_hive(hive=prism_co.hive, version=prism_co.version)
    test_lab(lab=prism_co.lab, version=prism_co.version)
    test_forge(forge=prism_co.forge, version=prism_co.version)

