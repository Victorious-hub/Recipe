from client.client import Client
from client.mock_client import MockClient
from core.enums import HandlerType
from core.handlers import CookingTimeHandler, UserIdFieldHandler
from dependency_injector import containers, providers
from schemas.recipe_schema import RecipeSchema


class Container(containers.DeclarativeContainer):
    """IoC container for dependency injection."""
    reqeust_handlers = {
        HandlerType.USER_ID_HANDLER_FIELD.value: UserIdFieldHandler(),
        HandlerType.COOKING_TIME_HANDLER_FIELD.value: CookingTimeHandler(),
    }
    data_schema = RecipeSchema
    base_api_url = "https://dummyjson.com/recipes"
    client = providers.Singleton(
        Client,
        base_url=base_api_url,
        data_schema=data_schema,
        handlers=reqeust_handlers
    )

    mock_client = providers.Singleton(
        MockClient,
        base_url=base_api_url,
        data_schema=data_schema,
        handlers=reqeust_handlers
    )
