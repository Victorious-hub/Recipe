from abc import ABC, abstractmethod

from schemas.base_schema import BaseSchema


class ABCClient(ABC):
    @abstractmethod
    def list_request_data(self, *args, **kwargs) -> list[BaseSchema]:
        raise NotImplementedError

    @abstractmethod
    def send_request_data(self, recipe) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_request_data(self, id: int) -> BaseSchema:
        raise NotImplementedError
