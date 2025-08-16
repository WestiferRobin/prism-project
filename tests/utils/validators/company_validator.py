from utils.validators.config_validators.comapny_configs import validate_company_config
from src.company import Company
from src.utils.configs.company_config import CompanyConfig


def validate_company(source_company: Company, target_company: Company):
    assert source_company is not None
    assert isinstance(source_company, Company)

    assert source_company.config is not None
    assert isinstance(source_company.config, CompanyConfig)
    validate_company_config(
        source_config=source_company.config,
        target_config=target_company.config
    )

