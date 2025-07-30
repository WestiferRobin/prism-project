from src.api import build_wes_config
from src.api.builders import build_mvp
from src.api.validators import validate_mvp
from src.utils.constants import INITIAL_VERSION


def test_initial_version(mvp: int = INITIAL_VERSION) -> None:
    mvp_users = get_initial_users()
    mvp = build_mvp(users=mvp_users)
    validate_mvp(mvp=mvp)


#
#
# def test_dev_version(mvp_version: int = INITIAL_VERSION) -> None:
#     dev_users = get_inital_users()
#     prism_net = build_mvp(mvp_version=DEV_VERSION, users=)
#     validate_mvp(mvp=prism_net, expected_version=DEV_VERSION)
#     test_platform(version=DEV_VERSION)
#
#
# def test_alpha_version(mvp_version: int = DEMO_VERSION) -> None:
#     demo_users = get_alpha_users()
#     mvp = build_mvp(version=mvp_version)
#     validate_mvp(mvp=prism_net, expected_version=DEMO_VERSION)
#     test_platform(version=DEMO_VERSION)
#
#
# def test_beta_version(mvp_version: int = 2) -> None:
#     beta_users = get_beta_users()
#     prism_net = build_mvp()
#
#
# def test_demo_versions() -> None:
#     test_alpha_versions()
#     test_beta_versions()
#
#
# def test_final_version(mvp_version: int = 3):
#     wes_config = build_wes_config(version=FINAL_VERSION)
#     prism_net = build_mvp(config=wes_config)
#     validate_mvp(mvp=prism_net, expected_version=FINAL_VERSION)
#     test_platform(version=FINAL_VERSION)
#
