from src.api import build_wes_config
from src.api.builders import build_mvp
from src.api.builders.config_builders import build_net_config
from src.utils.constants import INITIAL_VERSION


def test_wes_black(version: int = INITIAL_VERSION):
    wes_config = build_wes_config(version=version)
    net_config = build_net_config(version=version)
    mvp = build_mvp(case_config=wes_config)


def test_emma_cyan():
    pass


def test_mary_gold():
    pass


def test_max_red():
    pass


def test_tyler_green():
    pass


def test_payton_white():
    pass


def test_goose_omega():
    pass

