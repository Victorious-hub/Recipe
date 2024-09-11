from fastapi import APIRouter
from api.public import public_router

router = APIRouter(
    prefix="/api",
)

router.include_router(public_router)
