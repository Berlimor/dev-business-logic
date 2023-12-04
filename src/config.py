from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    manual_input: bool = False


settings = Settings()