import os
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

# Constants
MISSING_ENV = '>>> missing ENV value <<<'


class Config(BaseSettings):
    APP_ENV: str = os.getenv('APP_ENV', MISSING_ENV)
    DATABASE_USERNAME: str = os.getenv('DATABASE_USERNAME', MISSING_ENV)
    DATABASE_PASSWORD: str = os.getenv('DATABASE_PASSWORD', MISSING_ENV)
    DATABASE_HOST: str = os.getenv('DATABASE_HOST', MISSING_ENV)
    DATABASE_NAME: str = os.getenv('DATABASE_NAME', MISSING_ENV)
    TEST_DATABASE_NAME: str = os.getenv('DATABASE_NAME', MISSING_ENV)

    model_config = SettingsConfigDict(env_file=Path(__file__).parent / '.env')


config = Config()
