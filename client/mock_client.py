from client.base_client import ABCClient
from client.recipe_data import get_recipe_data
from schemas.base_schema import BaseSchema


class MockClient(ABCClient):
    def __init__(self, base_url: str, handlers: str, data_schema: BaseSchema) -> None:
        self.base_url = base_url
        self.data_schema = data_schema
        self.handlers = handlers
        self.request_data = get_recipe_data()

    def _apply_handlers(self, request: dict) -> str:
        handler_types = list(self.handlers.keys())
        for i in range(len(handler_types) - 1):
            self.handlers[handler_types[i]].successor = self.handlers[handler_types[i + 1]]
            self.handlers[handler_types[i]].handle(request)

    def send_request_data(self) -> None:
        self._apply_handlers(self.request_data)
        print("Request sent")

    def get_request_data(self) -> BaseSchema:
        return self.data_schema(**self.request_data)

    def list_request_data(self) -> list[BaseSchema]:
        return [self.data_schema(**self.request_data)]
