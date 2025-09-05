from src.models.app import App
from src.utils.configs.app_configs.lab_config import LabConfig


class Lab(App):
    lab_config: LabConfig

    def __init__(self, config: LabConfig, **lab_data):
        super().__init__(config=config, lab_config=config, **lab_data)

