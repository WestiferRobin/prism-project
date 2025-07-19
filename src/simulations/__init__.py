from pydantic import BaseModel

from src.exceptions import EngineException


class Simulation(BaseModel):
    name: str
    description: str
    root_path: str

    def __init__(self, name: str, description: str, root_path: str = "$") -> None:
        super().__init__(name=name, description=description, root_path=root_path)

    def run(self):
        print(f"Simulation {self.name}")
        is_running = True
        try:
            while is_running:
                is_running = self.handle_input()
        except EngineException as ex:
            print(ex)

