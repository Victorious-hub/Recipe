from client.client import Client
from fastapi import APIRouter, status, Depends
from api.dependencies import Container
from dependency_injector.wiring import Provide, inject
from schemas.pydantic.api_query_schema import RecipeQueryParamsApiSchema
from schemas.recipe_schema import RecipeSchema

recipe_router = APIRouter(
    prefix="/recipes",
    tags=["recipes"],
    responses={404: {"description": "Not found"}},
)


@recipe_router.get("/{id}", response_model=None, status_code=status.HTTP_200_OK)
@inject
async def get_recipe(
    id: int,
    client: Client = Depends(Provide[Container.client]),
) -> RecipeSchema:
    """Get recipe api"""
    return client.get_request_data(id)


@recipe_router.get("/", response_model=None, status_code=status.HTTP_200_OK)
@inject
async def list_recipes(
    query_params: RecipeQueryParamsApiSchema = Depends(),
    client: Client = Depends(Provide[Container.client]),
) -> RecipeSchema:
    """List recipes api"""
    params = {k: v for k, v in query_params.dict().items() if v is not None}
    recipe_list = client.list_request_data(**params)
    return [recipe.model_dump_exclude_null() for recipe in recipe_list]


@recipe_router.post("/", status_code=status.HTTP_201_CREATED)
@inject
async def create_recipe(
    recipe_data: dict,  # ! RecipeSchema won't work here. Need pydantic instance
    client: Client = Depends(Provide[Container.client]),
) -> None:
    """Create a new recipe api"""
    return client.send_request_data(request=recipe_data)
