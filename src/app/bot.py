from src.app import App


class Bot(App):
    def __init__(self, name: str, **app_data):
        super().__init__(name=name, **app_data)

