from src.api import build_wes_config
from src.api.builders import build_mvp
from src.utils.constants import LAMBDA_VERSION


if __name__ == '__main__':
    mvp_version = LAMBDA_VERSION
    wes_config = build_wes_config(version=mvp_version)
    mvp = build_mvp(version=mvp_version, user_configs=[wes_config])
    print(mvp)

