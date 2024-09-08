import json
from typing import TypeVar

import requests

from client.base_client import ABCClient
from schemas.base_schema import BaseSchema
from config.exceptions import RequestGetException, RequestPostException, RequestTimeoutException
from client.request_builder import DummyJsonQueryBuilder


class Client(ABCClient):
    def __init__(self, base_url: str, handlers: dict, data_schema: BaseSchema) -> None:
        self.base_url = base_url
        self.data_schema = data_schema
        self.handlers = handlers
        self.builder = DummyJsonQueryBuilder(base_url)

    def _apply_handlers(self, request: dict) -> str:
        """Check validation handlers for request"""
        handler_types = list(self.handlers.keys())
        for i in range(len(handler_types) - 1):
            self.handlers[handler_types[i]].successor = self.handlers[handler_types[i + 1]]
            self.handlers[handler_types[i]].handle(request)

    def send_request_data(self, request: dict) -> None:
        """Send post request"""
        self._apply_handlers(request)
        try:
            response = requests.post(self.base_url, json=json.dumps(request), timeout=5)
            if response.status_code != 201:
                raise RequestPostException
        except requests.exceptions.Timeout:
            raise RequestTimeoutException

    def get_request_data(self, id: int) -> BaseSchema:
        """Get request data"""
        try:
            response = requests.get(f"{self.base_url}/{id}", timeout=5)
        except requests.exceptions.Timeout:
            raise RequestTimeoutException
        else:
            if response.status_code == 200:
                return self.data_schema(**response.json())
            raise RequestGetException

    def list_request_data(self, *args, **kwargs) -> list[BaseSchema]:
        """List request data"""
        try:
            response = requests.get(self.builder.create_request_url(**kwargs), timeout=5)
        except requests.exceptions.Timeout:
            raise RequestTimeoutException
        else:
            result_response = response.json()[self.base_url.split("/")[-1]]
            if response.status_code == 200:
                return [self.data_schema(**result) for result in result_response]
            raise RequestGetException
