from src.app import App
from src.utils.configs.app_configs.game_config import GameConfig


class Game(App):
    game_config: GameConfig

    def __init__(self, config: GameConfig, **app_data):
        super().__init__(config=config, game_config=config, **app_data)

