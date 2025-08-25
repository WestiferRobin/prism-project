from src.app.terminals.web import WebTerminal
from src.utils.configs.app_configs.terminal_configs.mobile_config import MobileConfig


class MobileTerminal(WebTerminal):
    mobile_config: MobileConfig

    def __init__(self, config: MobileConfig, **terminal_data):
        super().__init__(
            config=config,
            mobile_config=config,
            **terminal_data
        )

