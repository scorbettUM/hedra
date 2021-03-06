from __future__ import annotations
from urllib.parse import urlparse
from typing import Any, Dict
from .request import Request
from .response import BaseResponse
from .history import History


class LastDict:

    def __init__(self) -> None:
        self._data = {}

    def __getitem__(self, name: str):
        return self._data.get(name, BaseResponse())
    
    def __setitem__(self, name: str, response: BaseResponse):
        self._data[name] = response


class Context:
    values = {}
    last: Dict[str, BaseResponse]  = LastDict()
    history = History()

    def __getitem__(self, key: str):
        return self.values.get(key)

    def __setitem__(self, key: str, value: str):
        self.values[key] = value

    def update_request(self, request: Request, context: Context = None):

        if context:
            self.values = {
                **context.values
            }

        request.name = self.values.get('name', request.name)

        updated_url = self.values.get('url', request.url.full)
        if request.url.full is None or request.url.full != updated_url:
            request.url.full = updated_url
            request.url.parsed = urlparse(updated_url)
            request.url.port = self.values.get('port', request.url.port)
        
        request.method = self.values.get('method', request.method)
        request.params.data = self.values.get('params', request.params.data)
        request.headers.data = self.values.get('headers', request.headers.data)
        request.payload.data = self.values.get('data', request.payload.data)
        request.metadata.tags = self.values.get('tags', request.metadata.tags)
        request.metadata.user = self.values.get('user', request.metadata.user)
        request.checks = self.values.get('checks', request.checks)
        request.is_setup = False

        return request
