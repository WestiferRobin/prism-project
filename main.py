from src.api.builders import build_mvp
from src.utils.constants import CURRENT_VERSION


if __name__ == '__main__':
    mvp = build_mvp(version=CURRENT_VERSION)
    print(mvp)

