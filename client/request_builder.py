from core.enums import (
    QueryBuilderFilter,
    QueryBuilderLimitSkip,
    QueryBuilderSearch,
    QueryBuilderSelect,
    QueryBuilderSort,
)
from core.exceptions import SortQueryException


class DummyJsonQueryBuilder:
    def __init__(self, client_base_url: str) -> None:
        self.client_base_url = client_base_url
        self.base_request_url = self.client_base_url

    def _build_query(self, query: str, base_separator: str) -> str:
        """Build query"""
        if self.base_request_url != self.client_base_url:
            return f"{self.base_request_url}&{query}"
        return f"{self.client_base_url}{base_separator}{query}"

    def _get_search_query(self, search: str) -> str:
        """Set search query param"""
        request_query = f"{QueryBuilderSearch.SEARCH.value}?q={search}"
        return self._build_query(request_query, "/")

    def _get_sort_query(self, sortBy: str, order: str | None) -> str:
        """Set sort query params"""
        if order not in QueryBuilderSort.SORT_ORDERING.value:
            raise SortQueryException

        request_query = f"{QueryBuilderSort.SORT.value}={sortBy}&{QueryBuilderSort.ORDER.value}={order}"
        return self._build_query(request_query, "?")

    def _get_limit_query(self, limit: int) -> str:
        """Set limit query param"""
        request_query = f"{QueryBuilderLimitSkip.LIMIT.value}={limit}"
        return self._build_query(request_query, "?")

    def _get_skip_query(self, skip: int) -> str:
        """Set skip query param"""
        request_query = f"{QueryBuilderLimitSkip.SKIP.value}={skip}"
        return self._build_query(request_query, "?")

    def _get_select_query(self, select: str) -> str:
        """Set select query param"""
        request_query = f"{QueryBuilderSelect.SELECT.value}={select}"
        return self._build_query(request_query, "?")

    def _get_filter_query(self, **kwargs) -> str:
        """Set filter query params"""
        filters = QueryBuilderFilter.get_filters()
        query_parts = None

        for value_filter in filters:
            if value_filter in kwargs:
                query = f"{value_filter}/{kwargs[value_filter]}"
                if query not in self.base_request_url:
                    query_parts = self._build_query(query, "/")
        return query_parts

    def _create_request_url(self, *args, **kwargs) -> str:
        """Create request url"""
        query_methods = {
            QueryBuilderLimitSkip.LIMIT.value: (self._get_limit_query, [QueryBuilderLimitSkip.LIMIT.value]),
            QueryBuilderLimitSkip.SKIP.value: (self._get_skip_query, [QueryBuilderLimitSkip.SKIP.value]),
            QueryBuilderSearch.SEARCH.value: (self._get_search_query, [QueryBuilderSearch.SEARCH.value]),
            QueryBuilderSort.SORT.value: (
                self._get_sort_query,
                [QueryBuilderSort.SORT.value, QueryBuilderSort.ORDER.value],
            ),
            QueryBuilderFilter.TAG.value: (self._get_filter_query, QueryBuilderFilter.get_filters()),
            QueryBuilderSelect.SELECT.value: (self._get_select_query, [QueryBuilderSelect.SELECT.value]),
        }

        for key, _ in query_methods.items():
            if key in kwargs.keys():
                func_exec, args = query_methods[key]
                self.base_request_url = func_exec(**{k: v for k, v in kwargs.items() if k in args})

        request = self.base_request_url
        self.base_request_url = self.client_base_url
        return request
