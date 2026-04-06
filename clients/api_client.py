import typing

from httpx import Client, Response
from httpx._types import RequestData, RequestFiles, QueryParamTypes, HeaderTypes
from httpx._urls import URL


class APIClient:
    def __init__(self, client: Client) -> None:
        self.client = client
        self.base_url = client.base_url

    def _request(self,
                 method: str,
                 url: URL | str,
                 *,
                 data: RequestData | None = None,
                 files: RequestFiles | None = None,
                 json: typing.Any | None = None,
                 params: QueryParamTypes | None = None,
                 headers: HeaderTypes | None = None) -> Response:
        return self.client.request(method, url, data=data, files=files, json=json, params=params, headers=headers)

    def get(self, *args, **kwargs) -> Response:
        return self._request('GET', *args, **kwargs)

    def post(self, *args, **kwargs) -> Response:
        return self._request('POST', *args, **kwargs)

    def put(self, *args, **kwargs) -> Response:
        return self._request('PUT', *args, **kwargs)

    def patch(self, *args, **kwargs) -> Response:
        return self._request('PATCH', *args, **kwargs)

    def delete(self, *args, **kwargs) -> Response:
        return self._request('DELETE', *args, **kwargs)
