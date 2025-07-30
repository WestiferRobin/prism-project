from typing import List

from acceptance.test_net.test_platforms import test_platform
from src.api import build_wes_config
from src.api.builders import build_mvp
from src.api.validators import validate_mvp
from src.utils.constants import DEV_VERSION, DEMO_VERSION, FINAL_VERSION, CURRENT_VERSION
from src.utils.user import User


def test_prism_net(users: List[User], version: int = CURRENT_VERSION):
    prism_net = build_mvp(users=users)
    validate_mvp(mvp=prism_net)




def test_dev_version():
    wes_config = build_wes_config(version=DEV_VERSION)
    prism_net = build_mvp(config=wes_config)
    validate_mvp(mvp=prism_net, expected_version=DEV_VERSION)
    test_platform(version=DEV_VERSION)


def test_demo_version():
    wes_config = build_wes_config(version=DEMO_VERSION)
    prism_net = build_mvp(config=wes_config)
    validate_mvp(mvp=prism_net, expected_version=DEMO_VERSION)
    test_platform(version=DEMO_VERSION)


def test_final_version():
    wes_config = build_wes_config(version=FINAL_VERSION)
    prism_net = build_mvp(config=wes_config)
    validate_mvp(mvp=prism_net, expected_version=FINAL_VERSION)
    test_platform(version=FINAL_VERSION)

