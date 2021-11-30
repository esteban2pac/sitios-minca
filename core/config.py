from pydantic import BaseSettings
from typing import Optional
from functools import lru_cache

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
  PROJECT_NAME: str = "Sitios en minca"
  POSTGRES_SERVER: str = "localhost"
  POSTGRES_USER: str = "fastapi"
  POSTGRES_PASSWORD: str = "123123"
  POSTGRES_DB: str = "minca"
  SQLALCHEMY_DATABASE_URI: Optional[str] = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"
  class Config:
      case_sensitive = True
 
@lru_cache
def get_settigns():
   return Settings()
 
settings = get_settigns()
