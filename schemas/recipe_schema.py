from typing import Optional
from schemas.base_schema import BaseSchema


class RecipeSchema(BaseSchema):
    id: Optional[int] = None
    name: Optional[str] = None
    ingredients: Optional[list[str]] = None
    instructions: Optional[list[str]] = None
    prepTimeMinutes: Optional[int] = None
    cookTimeMinutes: Optional[int] = None
    servings: Optional[int] = None
    difficulty: Optional[str] = None
    cuisine: Optional[str] = None
    caloriesPerServing: Optional[int] = None
    tags: Optional[list[str]] = None
    userId: Optional[int] = None
    image: Optional[str] = None
    rating: Optional[float] = None
    reviewCount: Optional[int] = None
    mealType: Optional[list[str]] = None
