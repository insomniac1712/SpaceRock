from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file= ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    #Application information
    APP_NAME: str = "SpaceRock"
    APP_VERSION: str = "0.1.0"

    #MongoDB
    MONGO_URI: str = "mongodb://localhost:27017"
    MONGO_DB: str = "spacerock"

    #NASA API
    NASA_API_KEY: str = "DEMO_KEY"
    NASA_API_BASE: str = "https://api.nasa.gov"
    NASA_RATE_LIMIT_RPM: int = 30
    
@lru_cache
def get_settings()->Settings:
    return Settings()