from src.app import App
from src.utils.configs.app_configs.studio_config import StudioConfig


class Studio(App):
    studio_config: StudioConfig

    def __init__(self, config: StudioConfig, **studio_data):
        super().__init__(config=config, studio_config=config, **studio_data)

