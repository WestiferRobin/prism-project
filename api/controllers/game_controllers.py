from api.controllers import Controller
from app.models import Command


class GameController(Controller):

    def read_request(self, command: Command) -> None:
        if isinstance(command, GameCommand):
            command.execute()

    def write_command(self) -> Command:
        pass