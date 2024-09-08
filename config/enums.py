from enum import Enum
from typing import Tuple


class SearchQuery(Enum):
    SEARCH = "search"


class SelectQuery(Enum):
    SELECT = "select"


class FilterQuery(Enum):
    TAGS = "tags"
    TAG = "tag"

    @staticmethod
    def get_filters() -> Tuple[str, str]:
        return (
            FilterQuery.TAGS.value,
            FilterQuery.TAG.value,
        )


class LimitSkipQuery(Enum):
    LIMIT = "limit"
    SKIP = "skip"


class SortQuery(Enum):
    SORT = "sortBy"
    ORDER = "order"


class HandlerType(Enum):
    USER_ID_HANDLER_FIELD = "user"
    COOKING_TIME_HANDLER_FIELD = "cook"


class QueryBuilderParams(Enum):
    SEARCH = "search"
    SORT_BY = "sort_by"
    ORDER = "order"
    LIMIT = "limit"
    SKIP = "skip"
    SELECT = "select"
    SORT_ORDERING = ["asc", "desc"]
