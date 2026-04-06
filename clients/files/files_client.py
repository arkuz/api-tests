from typing import TypedDict

from clients.private_http_client import get_private_http_client
from clients.test_app_client import TestAppAPIClient
from httpx import Response


class CreateFileRequestDict(TypedDict):
    filename: str
    directory: str
    upload_file: str


class FilesClient(TestAppAPIClient):
    endpoint = '/files'

    def upload_file(self, request: CreateFileRequestDict) -> Response:
        return self.post(url=f'{self.prefix}{self.endpoint}/',
                         data=request,
                         files={'upload_file': open(request['upload_file'], 'rb')})

    def get_file(self, file_id: str) -> Response:
        return self.get(url=f'{self.prefix}{self.endpoint}/{file_id}')

    def delete_file(self, file_id: str) -> Response:
        return self.delete(url=f'{self.prefix}{self.endpoint}/{file_id}')

def get_files_private_client() -> FilesClient:
    return FilesClient(client=get_private_http_client())
