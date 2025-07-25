from src.app import App


def validate_app(app: App) -> None:
    assert isinstance(app, App)

