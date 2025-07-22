from typing import cast

from app.models import Command
from app.models.commands import Response, Request
from app.models.commands.requests import PrismRequest


class PrismCommand(Command):

    def handle_standard_request(self, request: PrismRequest) -> Response:
        raise NotImplementedError()

    def execute(self, request: Request) -> None | Response:
        if isinstance(request, PrismRequest):
            prism_request = cast(PrismRequest, request)
            self.handle_standard_request(prism_request)
        else:
            raise NotImplementedError()
