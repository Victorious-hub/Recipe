import json
from schemas.base_schema import BaseSchema


class RecipeSchema(BaseSchema):
    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get("id")
        self.name = kwargs.get("name")
        self.ingredients = kwargs.get("ingredients")
        self.instructions = kwargs.get("instructions")
        self.prepTimeMinutes = kwargs.get("prepTimeMinutes")
        self.cookTimeMinutes = kwargs.get("cookTimeMinutes")
        self.servings = kwargs.get("servings")
        self.difficulty = kwargs.get("difficulty")
        self.cuisine = kwargs.get("cuisine")
        self.caloriesPerServing = kwargs.get("caloriesPerServing")
        self.tags = kwargs.get("tags")
        self.userId = kwargs.get("userId")
        self.image = kwargs.get("image")
        self.rating = kwargs.get("rating")
        self.reviewCount = kwargs.get("reviewCount")
        self.mealType = kwargs.get("mealType")

    def model_dump(self) -> dict:
        """Dump model to dictionary"""
        return self.__dict__

    def model_dump_exclude_null(self) -> dict:
        """Dump model to dictionary excluding None"""
        return {k: v for k, v in self.__dict__.items() if v is not None}

    def model_dump_json(self) -> str:
        """Dump model to json"""
        return json.dumps(self.__dict__)

    def __str__(self) -> str:
        """String representation of model"""
        output = ""
        for key, value in self.__dict__.items():
            output += f"{key} : {value}\n"
        return output
