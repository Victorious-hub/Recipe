from fastapi import APIRouter
from api.public.v1 import v1_router

public_router = APIRouter(
    prefix="/public",
)

public_router.include_router(v1_router)
