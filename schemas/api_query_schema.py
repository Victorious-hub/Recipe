
from typing import Optional

from core.enums import QueryBuilderSort
from schemas.base_schema import BaseSchema


class QueryParamsApiSchema(BaseSchema):
    limit: Optional[int] = None
    skip: Optional[int] = None
    sortBy: Optional[str] = None
    order: Optional[str] = QueryBuilderSort.SORT_ORDERING.value[0]
    select: Optional[str] = None
    search: Optional[str] = None


class RecipeQueryParamsApiSchema(QueryParamsApiSchema):
    tag: Optional[str] = None
