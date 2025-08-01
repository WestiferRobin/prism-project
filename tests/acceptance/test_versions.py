from src.api.builders import build_mvp
from src.api.services.user_service import get_initial_users, get_alpha_users, get_beta_users, get_demo_users, \
    get_final_users
from src.api.validators import validate_mvp
from src.utils.constants import DEV_VERSION, ALPHA_VERSION, BETA_VERSION, FINAL_VERSION, PROD_VERSION


def test_initial_version() -> None:
    mvp_users = get_initial_users()
    mvp = build_mvp(version=DEV_VERSION, users=mvp_users)
    validate_mvp(version=DEV_VERSION, mvp=mvp, users=mvp_users)


def test_alpha_version() -> None:
    mvp_users = get_alpha_users()
    mvp = build_mvp(version=ALPHA_VERSION, users=mvp_users)
    validate_mvp(version=ALPHA_VERSION, mvp=mvp, users=mvp_users)


def test_beta_version() -> None:
    mvp_users = get_beta_users()
    mvp = build_mvp(version=BETA_VERSION, users=mvp_users)
    validate_mvp(version=BETA_VERSION, mvp=mvp, users=mvp_users)


def test_demo_version() -> None:
    mvp_users = get_demo_users()
    mvp = build_mvp(version=FINAL_VERSION, users=mvp_users)
    validate_mvp(version=FINAL_VERSION, mvp=mvp, users=mvp_users)


def test_final_version() -> None:
    mvp_users = get_final_users()
    mvp = build_mvp(version=PROD_VERSION, users=mvp_users)
    validate_mvp(version=PROD_VERSION, mvp=mvp, users=mvp_users)

