from abc import ABC, abstractmethod

from core.enums import HandlerType
from core.handlers import DataFieldHandler


class ABCClient(ABC):
    def __init__(self, handlers: dict[HandlerType, DataFieldHandler]) -> None:
        self.handlers = handlers

    def _apply_request_handlers(self, request: dict) -> None:
        """Check validation handlers for request"""
        handler_types = list(self.handlers.keys())
        for i in range(len(handler_types) - 1):
            self.handlers[handler_types[i]].successor = self.handlers[handler_types[i + 1]]
            self.handlers[handler_types[i]].handle(request)

    @abstractmethod
    def fetch_list_data(self, *args, **kwargs) -> list[dict]:
        raise NotImplementedError

    @abstractmethod
    def send_request_data(self, request: dict) -> None:
        raise NotImplementedError

    @abstractmethod
    def fetch_data(self, id: int) -> dict:
        raise NotImplementedError
