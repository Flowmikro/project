from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Настройки проекта
    """
    database_url: str = "sqlite+aiosqlite:///./islam.db"


settings = Settings()
