from abc import ABC, abstractmethod
from typing import Optional

from core.exceptions import CookingTimeHandlerException, UserIdFieldHandlerException


class BaseRequestHandler(ABC):
    def __init__(self, successor: Optional["BaseRequestHandler"] = None) -> None:
        self.successor = successor

    def handle(self, request: dict) -> None:
        res = self.handle_request(request)
        if not res and self.successor:
            self.successor.handle(request)

    @abstractmethod
    def handle_request(self, request: int) -> Optional[bool]:
        raise NotImplementedError


class UserIdFieldHandler(BaseRequestHandler):
    @staticmethod
    def handle_request(request: dict) -> Optional[bool]:
        """Check if userId field is provided"""
        if request.get("userId") is None and request.get("name") is not None:
            raise UserIdFieldHandlerException


class CookingTimeHandler(BaseRequestHandler):
    @staticmethod
    def handle_request(request: dict) -> Optional[bool]:
        """Check if prepTimeMinutes field is provided"""
        if request.get("prepTimeMinutes") is None and request.get("cookTimeMinutes") is not None:
            raise CookingTimeHandlerException
