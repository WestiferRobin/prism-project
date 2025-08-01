from src.api.builders.company_builder import build_prism_co
from src.api.builders.config_builders.user_configs.wes_config import build_wes_config
from src.utils.constants import DEBUG_VERSION


if __name__ == '__main__':
    mvp_version = DEBUG_VERSION
    wes_config = build_wes_config(version=mvp_version)
    prism_co = build_prism_co(version=mvp_version, leader_config=wes_config)
    print(prism_co)

