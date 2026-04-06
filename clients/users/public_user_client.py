from httpx import Response

from clients.public_http_client import get_public_http_client
from clients.test_app_client import TestAppAPIClient
from clients.users.public_user_schema import CreateUserRequestSchema


class PublicUserClient(TestAppAPIClient):
    endpoint = '/users'

    def create_user(self, request: CreateUserRequestSchema) -> Response:
        return self.post(url=f'{self.prefix}{self.endpoint}', json=request.model_dump(by_alias=True))


def get_user_public_client() -> PublicUserClient:
    return PublicUserClient(client=get_public_http_client())
