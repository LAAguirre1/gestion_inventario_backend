import os

from dotenv import load_dotenv, find_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
load_dotenv(find_dotenv())


class Settings(BaseSettings):
    project_name: str = 'Gestión de Inventarios'
    algorithm: Optional[str] = os.getenv('ALGORITHM')
    access_token_expire_minutes: int = 60 * 24
    secret_key: Optional[str] = os.getenv('SECRET_KEY')
    database_url: str = 'sqlite:///./database.db'
    api_v1_str: str = '/api/v1'
    first_superuser: Optional[str] = os.getenv('FIRST_SUPERUSER')
    first_superuser_mail: Optional[str] = os.getenv('FIRST_SUPERUSER_EMAIL')
    first_superuser_password: Optional[str] = os.getenv('FIRST_SUPERUSER_PASSWORD')
    user_open_registration: bool = False
    backend_cors_origins: list[str] = [
        "http://localhost",
        "http://localhost:8080",
        "http://localhost:54642",
    ]


 #   model_config = SettingsConfigDict(env_file='.env')

settings = Settings()