from pydantic import BaseModel

from src.api.handlers.controller_handler import handle_input
from src.api.printers import print_model
from src.exceptions import EngineException
from src.models import Model


class Simulation(BaseModel):
    name: str
    description: str
    root_path: str
    model: Model = None

    def __init__(self, name: str, description: str, root_path: str = "$") -> None:
        super().__init__(name=name, description=description, root_path=root_path)

    def update(self):
        self.model.update()
        print_model(self.model)

    def run(self):
        print(f"Simulation {self.name}")
        is_running = True
        try:
            while is_running:
                self.update()
                is_running = handle_input(self.root_path)
        except EngineException as ex:
            print(ex)

    def add_model(self, model: Model):
        self.model = model
