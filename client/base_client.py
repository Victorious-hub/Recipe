from abc import ABC, abstractmethod


class ABCClient(ABC):
    @abstractmethod
    def fetch_list_request_data(self, *args, **kwargs) -> list[dict]:
        raise NotImplementedError

    @abstractmethod
    def send_request_data(self, request: dict) -> None:
        raise NotImplementedError

    @abstractmethod
    def fetch_request_data(self, id: int) -> dict:
        raise NotImplementedError

    @abstractmethod
    def _apply_request_handlers(self, request: dict) -> None:
        raise NotImplementedError
