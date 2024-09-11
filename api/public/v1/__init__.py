from fastapi import APIRouter
from .recipe import recipe_router

v1_router = APIRouter(
    prefix="/v1",
)

v1_router.include_router(recipe_router)
