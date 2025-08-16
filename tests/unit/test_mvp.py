from typing import List

from src.api.builders import build_mvp
from utils import validate_mvp
from src.utils.constants import DEV_VERSION
from src.utils.user import User


def test_prism_net(users: List[User], version: int = DEV_VERSION):
    prism_net = build_mvp(users=users)
    validate_mvp(,,
