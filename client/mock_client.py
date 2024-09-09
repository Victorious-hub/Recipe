import logging
from typing import Generic
from client.base_client import ABCClient, T
from client.recipe_data import get_mock_recipe_data, list_mock_recipe_data
from core.enums import HandlerType
from core.handlers import BaseRequestHandler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MockClient(ABCClient[T], Generic[T]):
    def __init__(self, base_url: str, handlers: dict[HandlerType, BaseRequestHandler], data_schema: T) -> None:
        self.base_url = base_url
        self.data_schema = data_schema
        self.handlers = handlers
        self.request_list_data = list_mock_recipe_data()
        self.request_data = get_mock_recipe_data()

    def _apply_request_handlers(self, request: dict) -> None:
        """Check validation handlers for request"""
        handler_types = list(self.handlers.keys())
        for i in range(len(handler_types) - 1):
            self.handlers[handler_types[i]].successor = self.handlers[handler_types[i + 1]]
            self.handlers[handler_types[i]].handle(request)

    def send_request_data(self) -> None:
        """Mock post request"""
        self._apply_request_handlers(self.request_data)
        logger.info(f"Mock request data sent: {self.request_data}")

    def get_request_data(self, id: int = 1) -> T:
        """Mock get request data"""
        return self.data_schema(**self.request_data)

    def list_request_data(self) -> list[T]:
        """List request data"""
        return [self.data_schema(**result) for result in self.request_list_data]
