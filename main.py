from src.api import build_wes_config
from src.api.builders import build_mvp
from src.utils.constants import INITIAL_VERSION


if __name__ == '__main__':
    user = build_wes_config(version=INITIAL_VERSION)
    mvp = build_mvp(user)
    print(mvp)

