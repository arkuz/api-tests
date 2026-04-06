from pydantic_settings import BaseSettings, SettingsConfigDict


class MyBaseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')


class HTTPClientSettings(MyBaseSettings):
    model_config = SettingsConfigDict(env_prefix="HTTP_CLIENT_")

    base_url: str
    timeout: int


class Settings(MyBaseSettings):
    http_client: HTTPClientSettings = HTTPClientSettings()
