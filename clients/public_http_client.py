from httpx import Client

from settings import Settings

settings = Settings()


def get_public_http_client() -> Client:
    return Client(base_url=settings.http_client.base_url,
                  timeout=settings.http_client.timeout)
