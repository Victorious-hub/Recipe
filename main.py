from api.dependencies import Container
from api import router as api_router_v1
from api.public.v1 import recipe
from fastapi import FastAPI
from core.config import settings


def create_application():
    """Create and configure the FastAPI application."""
    container = Container()
    application = FastAPI(docs_url="/api/docs")
    if settings.CLIENT.RECIPES_API_MOCK:
        container.client.override(container.mock_client)
    container.wire(modules=[recipe])
    application.include_router(api_router_v1)
    return application


app = create_application()
