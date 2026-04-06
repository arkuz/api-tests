from httpx import Response

from clients.auth.auth_schema import LoginRequestSchema, RefreshRequestSchema, LoginResponseSchema
from clients.public_http_client import get_public_http_client
from clients.test_app_client import TestAppAPIClient


class AuthenticationClient(TestAppAPIClient):
    endpoint = '/authentication'

    def login_api(self, request: LoginRequestSchema) -> Response:
        return self.post(url=f'{self.prefix}{self.endpoint}/login', json=request.model_dump())

    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        return self.post(url=f'{self.prefix}{self.endpoint}/refresh', json=request)

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        response = self.login_api(request=request)
        return LoginResponseSchema.model_validate_json(response.text)


def get_auth_public_client() -> AuthenticationClient:
    return AuthenticationClient(client=get_public_http_client())
