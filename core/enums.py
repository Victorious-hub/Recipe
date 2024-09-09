from enum import Enum
from typing import Tuple


class QueryBuilderSearch(Enum):
    """Search query builder enum"""
    SEARCH = "search"


class QueryBuilderSelect(Enum):
    """Select query builder enum"""
    SELECT = "select"


class QueryBuilderFilter(Enum):
    """Filter query builder enum"""
    TAG = "tag"

    @staticmethod
    def get_filters() -> tuple[str]:
        return (QueryBuilderFilter.TAG.value,)


class QueryBuilderLimitSkip(Enum):
    """Limit and skip query builder enum"""
    LIMIT = "limit"
    SKIP = "skip"


class QueryBuilderSort(Enum):
    """Sort query builder enum"""
    SORT = "sortBy"
    ORDER = "order"
    SORT_ORDERING = ["asc", "desc"]


class HandlerType(Enum):
    """Handler type enum"""
    USER_ID_HANDLER_FIELD = "user"
    COOKING_TIME_HANDLER_FIELD = "cook"
