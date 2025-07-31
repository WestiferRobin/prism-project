from src.api.builders import build_mvp
from src.api.services.user_service import get_initial_users, get_alpha_users, get_beta_users, get_demo_users, \
    get_final_users
from src.api.validators import validate_mvp
from src.utils.constants import LAMBDA_VERSION, ALPHA_VERSION, BETA_VERSION, GAMMA_VERSION, OMEGA_VERSION


def test_initial_version() -> None:
    mvp_users = get_initial_users()
    mvp = build_mvp(version=LAMBDA_VERSION, users=mvp_users)
    validate_mvp(version=LAMBDA_VERSION, mvp=mvp, users=mvp_users)


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
    mvp = build_mvp(version=GAMMA_VERSION, users=mvp_users)
    validate_mvp(version=GAMMA_VERSION, mvp=mvp, users=mvp_users)


def test_final_version() -> None:
    mvp_users = get_final_users()
    mvp = build_mvp(version=OMEGA_VERSION, users=mvp_users)
    validate_mvp(version=OMEGA_VERSION, mvp=mvp, users=mvp_users)

