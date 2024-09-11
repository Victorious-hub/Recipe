import logging
from typing import Generic, Optional
from client.base_client import ABCClient
from client.recipe_data import get_mock_recipe_data, list_mock_recipe_data
from core.enums import HandlerType
from core.handlers import DataFieldHandler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MockClient(ABCClient):
    def __init__(self, base_url: str, handlers: dict[HandlerType, DataFieldHandler]) -> None:
        super().__init__(handlers)
        self.base_url = base_url
        self.request_list_data = list_mock_recipe_data()
        self.request_data = get_mock_recipe_data()

    def send_request_data(self, request: Optional[dict] = None) -> None:
        """Mock post request"""
        self._apply_request_handlers(self.request_data)
        logger.info(f"Mock request data sent: {self.request_data}")

    def fetch_data(self, id: Optional[int] = 1) -> dict:
        """Mock get request data"""
        return self.request_data

    def fetch_list_data(self, *args, **kwargs) -> list[dict]:
        """List request data"""
        return self.request_list_data
