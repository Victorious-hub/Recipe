class SortQueryException(Exception):
    def __init__(self, message="Order field is not provided or invalid") -> None:
        self.message = message
        super().__init__(self.message)


class UserIdFieldHandlerException(Exception):
    def __init__(self, message="userId is required") -> None:
        self.message = message
        super().__init__(self.message)


class CookingTimeHandlerException(Exception):
    def __init__(self, message="prepTimeMinutes is required") -> None:
        self.message = message
        super().__init__(self.message)


class RequestGetException(Exception):
    def __init__(self, message="Error to get data") -> None:
        self.message = message
        super().__init__(self.message)


class RequestPostException(Exception):
    def __init__(self, message="Error to create data") -> None:
        self.message = message
        super().__init__(self.message)


class RequestTimeoutException(Exception):
    def __init__(self, message="Timeout error") -> None:
        self.message = message
        super().__init__(self.message)
