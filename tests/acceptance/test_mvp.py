from src.api.builders.company_builder import build_prism_co, build_company
from src.api.builders.config_builders.user_configs.wes_config import build_wes_config
from src.utils.constants import DEBUG_VERSION, DEV_VERSION, TEST_VERSION, PROD_VERSION, FINAL_VERSION
from utils.validators.company_validator import validate_company


def test_debug_version():
    prism_co = build_prism_co(
        version=DEBUG_VERSION,
        leader_config=build_wes_config(version=DEBUG_VERSION)
    )
    validate_company(
        source_company=prism_co,
        target_company=build_company(
            version=prism_co.config.version,
            company_name=prism_co.config.name,
            leader_config=prism_co.config.leader_config
        )
    )


def test_dev_version():
    prism_co = build_prism_co(
        version=DEV_VERSION,
        leader_config=build_wes_config(version=DEV_VERSION)
    )
    validate_company(
        source_company=prism_co,
        target_company=build_company(
            version=prism_co.config.version,
            company_name=prism_co.config.name,
            leader_config=prism_co.config.leader_config
        )
    )


def test_test_version():
    prism_co = build_prism_co(
        version=TEST_VERSION,
        leader_config=build_wes_config(version=TEST_VERSION)
    )
    validate_company(
        source_company=prism_co,
        target_company=build_company(
            version=prism_co.config.version,
            company_name=prism_co.config.name,
            leader_config=prism_co.config.leader_config
        )
    )


def test_prod_version():
    prism_co = build_prism_co(
        version=PROD_VERSION,
        leader_config=build_wes_config(version=PROD_VERSION)
    )
    validate_company(
        source_company=prism_co,
        target_company=build_company(
            version=prism_co.config.version,
            company_name=prism_co.config.name,
            leader_config=prism_co.config.leader_config
        )
    )


def test_final_version():
    prism_co = build_prism_co(
        version=FINAL_VERSION,
        leader_config=build_wes_config(version=FINAL_VERSION)
    )
    validate_company(
        source_company=prism_co,
        target_company=build_company(
            version=prism_co.config.version,
            company_name=prism_co.config.name,
            leader_config=prism_co.config.leader_config
        )
    )

