from src.app import App
from src.utils.configs.app_configs.tool_config import ToolConfig


class Tool(App):
    def __init__(self, config: ToolConfig, **tool_data):
        super().__init__(config=config, **tool_data)

