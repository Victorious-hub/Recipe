import json

import requests

from client.base_client import ABCClient
from core.enums import HandlerType
from core.handlers import DataFieldHandler
from core.exceptions import RequestGetException, RequestPostException, RequestTimeoutException
from client.request_builder import DummyJsonQueryBuilder


class Client(ABCClient):
    def __init__(self, base_url: str, handlers: dict[HandlerType, DataFieldHandler]) -> None:
        self.base_url = base_url
        self.handlers = handlers
        self.builder = DummyJsonQueryBuilder(base_url)

    def _apply_request_handlers(self, request: dict) -> None:
        """Check validation handlers for request"""
        handler_types = list(self.handlers.keys())
        for i in range(len(handler_types) - 1):
            self.handlers[handler_types[i]].successor = self.handlers[handler_types[i + 1]]
            self.handlers[handler_types[i]].handle(request)

    def send_request_data(self, request: dict) -> None:
        """Send post request"""
        self._apply_request_handlers(request)
        try:
            response = requests.post(self.base_url, json=json.dumps(request), timeout=5)
            if response.status_code != 201:
                raise RequestPostException
        except requests.exceptions.Timeout:
            raise RequestTimeoutException

    def fetch_request_data(self, id: int) -> dict:
        """Fetch request data"""
        try:
            response = requests.get(f"{self.base_url}/{id}", timeout=5)
            if response.status_code == 200:
                return response.json()
            raise RequestGetException
        except requests.exceptions.Timeout:
            raise RequestTimeoutException

    def fetch_list_request_data(self, *args, **kwargs) -> list[dict]:
        """Fetch List request data"""
        try:
            response = requests.get(self.builder.create_request_url(**kwargs), timeout=5)
            result_list_response = response.json()[self.base_url.split("/")[-1]]
            if response.status_code == 200:
                return result_list_response
            raise RequestGetException
        except requests.exceptions.Timeout:
            raise RequestTimeoutException
