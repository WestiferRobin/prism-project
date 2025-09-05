from src.models.app.terminals import Terminal
from src.utils.configs.app_configs.terminal_configs.web_config import WebConfig


class WebTerminal(Terminal):
    web_config: WebConfig

    def __init__(self, config: WebConfig, **terminal_data):
        super().__init__(
            config=config,
            web_config=config,
            **terminal_data,
        )


