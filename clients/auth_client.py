from typing import TypedDict

from httpx import Response

from clients.test_app_client import TestAppAPIClient


class LoginRequestDict(TypedDict):
    email: str
    password: str


class RefreshRequestDict(TypedDict):
    refreshToken: str


class AuthenticationClient(TestAppAPIClient):
    endpoint = '/authentication'

    def login(self, request: LoginRequestDict) -> Response:
        return self.post(url=f'{self.prefix}{self.endpoint}/login', json=request)

    def refresh(self, request: RefreshRequestDict) -> Response:
        return self.post(url=f'{self.prefix}{self.endpoint}/refresh', json=request)
