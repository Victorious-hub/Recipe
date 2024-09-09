from fastapi import HTTPException


class ServiceException(HTTPException):
    """Base class for service exceptions"""
    def __init__(self, detail: str, status_code: int = 400) -> None:
        self.status_code = status_code
        self.detail = detail


class SortQueryException(ServiceException):
    """Exception for sort query"""
    def __init__(self) -> None:
        super().__init__(detail="Order field is not provided or invalid")


class UserIdFieldHandlerException(ServiceException):
    """Exception for userId field"""
    def __init__(self) -> None:
        super().__init__(detail="userId is required")


class CookingTimeHandlerException(ServiceException):
    """Exception for prepTimeMinutes field"""
    def __init__(self) -> None:
        super().__init__(detail="prepTimeMinutes is required")


class RequestGetException(ServiceException):
    """Exception for get request"""
    def __init__(self) -> None:
        super().__init__(detail="Error to get data")


class RequestPostException(ServiceException):
    """Exception for post request"""
    def __init__(self) -> None:
        super().__init__(detail="Error to create data")


class RequestTimeoutException(ServiceException):
    """Exception for request timeout"""
    def __init__(self) -> None:
        super().__init__(detail="Timeout error")
