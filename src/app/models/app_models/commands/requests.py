from src.utils.enums import RequestType

class Request:
    type: RequestType = RequestType.Standard


class PrismRequest(Request):
    def __init__(self, **request_data):
        super().__init__(**request_data)

