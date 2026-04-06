from clients.api_client import APIClient
from httpx import Client


class TestAppAPIClient(APIClient):
    def __init__(self, client: Client) -> None:
        super().__init__(client)
        self.prefix = "/api/v1"
