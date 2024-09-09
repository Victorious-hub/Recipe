
from typing import Optional
from pydantic import BaseModel

from core.enums import QueryBuilderSort


class QueryParamsApiSchema(BaseModel):
    limit: Optional[int] = None
    skip: Optional[int] = None
    sortBy: Optional[str] = None
    order: Optional[str] = QueryBuilderSort.SORT_ORDERING.value[0]
    select: Optional[str] = None
    search: Optional[str] = None


class RecipeQueryParamsApiSchema(QueryParamsApiSchema):
    tag: Optional[str] = None
