from api.dependencies import Container
from api import recipe
from fastapi import FastAPI
from core.config import settings


def create_application():
    """Create and configure the FastAPI application."""
    container = Container()
    application = FastAPI(docs_url="/api/docs")
    if settings.CLIENT.RECIPES_API_MOCK:
        container.client.override(container.mock_client)
    container.wire(modules=[recipe])
    application.include_router(recipe.recipe_router)
    return application


app = create_application()
