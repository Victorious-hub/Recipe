import os
from client.client import Client
from client.recipe_data import get_recipe_data
from config.enums import HandlerType
from config.handlers import CookingTimeHandler, UserIdFieldHandler
from client.mock_client import MockClient
from schemas.recipe_schema import RecipeSchema
from config.config import settings

if __name__ == "__main__":
    handler = {
        HandlerType.USER_ID_HANDLER_FIELD.value: UserIdFieldHandler(),
        HandlerType.COOKING_TIME_HANDLER_FIELD.value: CookingTimeHandler(),
    }
    recipe_schema = RecipeSchema
    base_url = "https://dummyjson.com/recipes"

    if settings.CLIENT.RECIPES_API_MOCK is True:
        mock_client = MockClient(base_url, handler, recipe_schema)
        mocked_result = mock_client.get_request_data()
        print(mocked_result)
        mock_client.send_request_data()
    else:
        data = get_recipe_data()
        client = Client(base_url, handler, recipe_schema)
        list_result = client.list_request_data(sortBy="name", order="desc", limit=10)
        for result in list_result:
            print(result)
        client.send_request_data(request=data)
