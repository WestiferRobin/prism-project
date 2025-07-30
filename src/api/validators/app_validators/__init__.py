from src.app import App
from src.utils.enums.platform_enums import PlatformType


def validate_app(app: App, expected_platform: PlatformType) -> None:
    assert isinstance(app, App)
    assert app.platform == expected_platform

