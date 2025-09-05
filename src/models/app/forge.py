from src.models.app import App
from src.utils.configs.app_configs.forge_config import ForgeConfig


class Forge(App):
    forge_config: ForgeConfig

    def __init__(self, config: ForgeConfig, **forge_data):
        super().__init__(config=config, forge_config=config, **forge_data)

