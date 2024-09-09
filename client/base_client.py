from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from schemas.base_schema import BaseSchema

T = TypeVar("T", bound=BaseSchema)


class ABCClient(ABC, Generic[T]):
    @abstractmethod
    def list_request_data(self, *args, **kwargs) -> list[T]:
        raise NotImplementedError

    @abstractmethod
    def send_request_data(self, request: dict) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_request_data(self, id: int) -> T:
        raise NotImplementedError
