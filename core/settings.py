from pydantic import BaseSettings
from secrets import token_urlsafe

class Settings(BaseSettings):
    SECRET_KEY: str = token_urlsafe(32)
    PROJECT_NAME: str
    DATABASE_URL: str
   
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()