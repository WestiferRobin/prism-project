from typing import List
from uuid import UUID

from src.api.helpers.registry_helper import configure_app_registry
from src.app import App
from src.utils.exceptions import PrismException


def configure_apps(version: int, user_id: UUID) -> List[App]:
    app_registry = configure_app_registry(version=version)
    if user_id not in app_registry:
        raise PrismException(f"User not found in planned app registry for {user_id}")
    return app_registry[user_id]