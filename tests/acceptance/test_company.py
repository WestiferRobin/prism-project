from src.api.builders.company_builder import build_prism_co, build_company
from src.api.builders.config_builders.user_configs.wes_config import build_wes_config
from src.api.validators.company_validator import validate_company
from src.utils.constants import DEBUG_VERSION


def test_prism_co():
    leader_config = build_wes_config(version=DEBUG_VERSION)
    prism_co = build_prism_co(
        version=DEBUG_VERSION,
        leader_config=leader_config
    )
    company = build_company(
        version=DEBUG_VERSION,
        company_name="Prism Co",
        leader_config=leader_config
    )
    validate_company(source_company=prism_co, target_company=company)

