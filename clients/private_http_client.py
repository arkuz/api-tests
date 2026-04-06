from httpx import Client

from clients.auth.auth_client import get_auth_public_client
from clients.auth.auth_schema import LoginRequestSchema
from settings import Settings

settings = Settings()


def get_private_http_client(request: LoginRequestSchema) -> Client:
    auth_public_client = get_auth_public_client()
    login_response_schema = auth_public_client.login(request)
    access_token = login_response_schema.token.access_token

    return Client(base_url=settings.http_client.base_url,
                  timeout=settings.http_client.timeout,
                  headers={'Authorization': f'Bearer {access_token}'})
