from src.api.validators.config_validators import validate_app_config
from src.models.app import App


def validate_app(
    source_app: App,
    target_app: App,
    ignore_id: bool = True,
    ignore_name: bool = True
) -> None:
    assert isinstance(source_app, App)

    assert source_app.config is not None
    validate_app_config(
        source_config=source_app.config,
        target_config=target_app.config,
        ignore_id=ignore_id,
        ignore_name=ignore_name
    )

    if not ignore_id:
        assert source_app.id == target_app.id
    if not ignore_name:
        assert source_app.name.lower() == target_app.name.lower()


def validate_studio(source_studio: App, target_studio: App) -> None:
    validate_app(
        source_app=source_studio,
        target_app=target_studio,
        ignore_id=False,
        ignore_name=False
    )


def validate_hive(source_hive: App, target_hive: App) -> None:
    validate_app(
        source_app=source_hive,
        target_app=target_hive,
        ignore_id=False,
        ignore_name=False
    )


def validate_lab(source_lab: App, target_lab: App) -> None:
    validate_app(
        source_app=source_lab,
        target_app=target_lab,
        ignore_id=False,
        ignore_name=False
    )


def validate_forge(source_forge: App, target_forge: App) -> None:
    validate_app(
        source_app=source_forge,
        target_app=target_forge,
        ignore_id=False,
        ignore_name=False
    )

