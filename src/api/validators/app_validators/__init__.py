from src.app import App
from src.utils.enums.platform_enums import PlatformType


def validate_app(app: App, target_platform: PlatformType) -> None:
    assert isinstance(app, App)
    assert app.platform == target_platform

