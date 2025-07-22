from typing import cast

from zlegacy.app.models import Command
from zlegacy.app.models import Response, Request
from src.app.models.app_models.commands.requests import PrismRequest


class PrismCommand(Command):

    def handle_standard_request(self, request: PrismRequest) -> Response:
        raise NotImplementedError()

    def execute(self, request: Request) -> None | Response:
        if isinstance(request, PrismRequest):
            prism_request = cast(PrismRequest, request)
            self.handle_standard_request(prism_request)
        else:
            raise NotImplementedError()
