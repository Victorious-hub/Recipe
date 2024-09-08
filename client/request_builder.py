from enum import Enum
from config.enums import FilterQuery, LimitSkipQuery, QueryBuilderParams, SearchQuery, SortQuery
from config.exceptions import SortQueryException


class DummyJsonQueryBuilder:
    def __init__(self, client_base_url: str) -> None:
        self.client_base_url = client_base_url
        self.base_request = self.client_base_url

    def _build_query(self, query: str, base_separator: str) -> str:
        if self.base_request != self.client_base_url:
            return f"{self.base_request}&{query}"
        return f"{self.client_base_url}{base_separator}{query}"

    def get_search_query(self, search: str) -> str:
        request_query = f"{QueryBuilderParams.SEARCH.value}?q={search}"
        return self._build_query(request_query, "/")

    def get_sort_query(self, sortBy: str, order: str | None) -> str:
        if order not in QueryBuilderParams.SORT_ORDERING.value:
            raise SortQueryException

        request_query = f"{QueryBuilderParams.SORT_BY.value}={sortBy}&{QueryBuilderParams.ORDER.value}={order}"
        return self._build_query(request_query, "?")

    def get_limit_query(self, limit: int) -> str:
        request_query = f"{QueryBuilderParams.LIMIT.value}={limit}"
        return self._build_query(request_query, "?")

    def get_skip_query(self, skip: int) -> str:
        request_query = f"{QueryBuilderParams.SKIP.value}={skip}"
        return self._build_query(request_query, "?")

    def get_select_query(self, select: str) -> str:
        request_query = f"{QueryBuilderParams.SELECT.value}={select}"
        return self._build_query(request_query, "?")

    def get_filter_query(self, **kwargs) -> str:
        filters = FilterQuery.get_filters()
        query_parts = None

        for value_filter in filters:
            if value_filter in kwargs:
                query = f"{filter}={kwargs[filter]}"
                if query not in self.base_request:
                    query_parts = self._build_query(query, "/")
        return query_parts

    def create_request_url(self, *args, **kwargs):
        query_methods = {
            LimitSkipQuery.LIMIT.value: (self.get_limit_query, [LimitSkipQuery.LIMIT.value]),
            LimitSkipQuery.SKIP.value: (self.get_skip_query, [LimitSkipQuery.SKIP.value]),
            SearchQuery.SEARCH.value: (self.get_search_query, [SearchQuery.SEARCH.value]),
            SortQuery.SORT.value: (self.get_sort_query, [SortQuery.SORT.value, SortQuery.ORDER.value]),
            FilterQuery.TAG.value: (self.get_filter_query, FilterQuery.get_filters()),
            FilterQuery.TAGS.value: (self.get_filter_query, FilterQuery.get_filters()),
        }

        for key, _ in query_methods.items():
            if key in kwargs.keys():
                func_exec, args = query_methods[key]
                self.base_request = func_exec(**{k: v for k, v in kwargs.items() if k in args})

        request = self.base_request
        self.base_request = self.client_base_url
        return request
