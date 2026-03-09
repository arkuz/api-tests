from clients.api_client import APIClient
from httpx import Client
from httpx._urls import URL


class TestAppAPIClient(APIClient):
    def __init__(self, client: Client, base_url: URL | str) -> None:
        super().__init__(client, base_url)
        self.prefix = "/api/v1"
