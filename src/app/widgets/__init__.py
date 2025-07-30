from src.app import App
from src.utils.configs.app_configs.widget_config import WidgetConfig


class Widget(App):
    def __init__(self, config: WidgetConfig, **widget_data):
        super().__init__(config=config, app_data=widget_data)

