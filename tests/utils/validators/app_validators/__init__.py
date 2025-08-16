from utils.validators.config_validators import validate_config
from src.app import App
from src.utils.configs.app_configs import AppConfig


def validate_app_config(
    app_config: AppConfig,
    expected_config: AppConfig,
    ignore_id: bool = True,
    ignore_name: bool = True
) -> None:
    assert isinstance(app_config, AppConfig)

    assert app_config.platform_type == expected_config.platform_type
    assert len(app_config.accounts) == len(expected_config.accounts)

    validate_config(
        source_config=app_config,
        target_config=expected_config,
        ignore_id=ignore_id,
        ignore_name=ignore_name
    )


def validate_app(
    app: App,
    expected_app: App,
    ignore_id: bool = True,
    ignore_name: bool = True
) -> None:
    assert isinstance(app, App)

    assert app.config is not None
    validate_app_config(
        app_config=app.config,
        expected_config=expected_app.config,
        ignore_id=ignore_id,
        ignore_name=ignore_name
    )

    if not ignore_id:
        assert app.id == expected_app.id
    if not ignore_name:
        assert app.name.lower() == expected_app.name.lower()



def validate_lab(lab: App, expected_app: App) -> None:
    validate_app(
        app=lab,
        expected_app=expected_app,
        ignore_id=False,
        ignore_name=False
    )



def validate_studio(studio: App, expected_app: App) -> None:
    validate_app(
        app=studio,
        expected_app=expected_app,
        ignore_id=False,
        ignore_name=False
    )


def validate_forge(forge: App, expected_app: App) -> None:
    validate_app(
        app=forge,
        expected_app=expected_app,
        ignore_id=False,
        ignore_name=False
    )


def validate_hive(hive: App, expected_app: App) -> None:
    validate_app(
        app=hive,
        expected_app=expected_app,
        ignore_id=False,
        ignore_name=False
    )

