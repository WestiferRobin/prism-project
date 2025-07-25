from src.app import App
from src.models.prisms import Prism


class Drone(App):
    prism: Prism

    def __init__(self, prism: Prism, **drone_data):
        super().__init__(prism=prism,name=prism.name, **drone_data)

