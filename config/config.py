from functools import lru_cache
import os
from typing import List
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from pathlib import Path
from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class ClientSettings(BaseModel):
    RECIPES_API_MOCK: bool


class Settings(BaseSettings):
    CLIENT: ClientSettings
    model_config = SettingsConfigDict(env_file=".env", env_nested_delimiter="__")


settings = Settings()
