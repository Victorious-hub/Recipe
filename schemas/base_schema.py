from abc import ABC, abstractmethod


class BaseSchema(ABC):
    @abstractmethod
    def model_dump() -> dict:
        raise NotImplementedError

    @abstractmethod
    def model_dump_json() -> str:
        raise NotImplementedError
