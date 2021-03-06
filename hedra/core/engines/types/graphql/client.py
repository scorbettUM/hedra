import asyncio
from types import FunctionType
from hedra.core.engines.types.common.types import RequestTypes
from hedra.core.engines.types.http2 import MercuryHTTP2Client
from hedra.core.engines.types.http import MercuryHTTPClient
from hedra.core.engines.types.common import Timeouts
from hedra.core.engines.types.common.context import Context
from hedra.core.engines.types.common import Request, Response
from typing import Awaitable, List, Union, Tuple, Set, Optional
from async_tools.datatypes import AsyncList


GraphQLResponseFuture = Awaitable[Union[Response, Exception]]
GraphQLBatchResponseFuture = Awaitable[Tuple[Set[GraphQLResponseFuture], Set[GraphQLResponseFuture]]]


class MercuryGraphQLClient:

    def __init__(self, concurrency: int = 10 ** 3, timeouts: Timeouts = Timeouts(), hard_cache=False, use_http2=False, reset_connection: bool=False) -> None:
        
        if use_http2:
            self.protocol = MercuryHTTP2Client(
                concurrency=concurrency,
                timeouts=timeouts,
                hard_cache=hard_cache,
                reset_connections=reset_connection
            )
        
        else:
            self.protocol = MercuryHTTPClient(
                concurrency=concurrency,
                timeouts=timeouts,
                hard_cache=hard_cache,
                reset_connections=reset_connection
            )
        
        self._use_http2 = use_http2
        self.context = Context()
        self.protocol.context = self.context
        self.registered = {}

    async def prepare(self, request: Request) -> Awaitable[None]:
        try:
            if request.url.is_ssl:
                request.ssl_context = self.protocol.ssl_context

            if self.protocol._hosts.get(request.url.hostname) is None:
                    self.protocol._hosts[request.url.hostname] = await request.url.lookup()
            else:
                request.url.ip_addr = self.protocol._hosts[request.url.hostname]

            if request.is_setup is False:
                request.setup_graphql_request(use_http2=self._use_http2)

            self.protocol.registered[request.name] = request
            self.registered[request.name] = request
        
        except Exception as e:
            return e

    async def execute_prepared_request(self, request: Request):
        response: Response = await self.protocol.execute_prepared_request(request)
        response.type = RequestTypes.GRAPHQL

        self.context.last[request.name] = self.protocol.context.last[request.name]
        return response

    async def request(self, request: Request) -> GraphQLResponseFuture:
        return await self.execute_prepared_request(request.name)
        
    async def execute_batch(
        self, 
        request: Request,
        concurrency: Optional[int]=None, 
        timeout: Optional[float]=None
    ) -> GraphQLBatchResponseFuture:
    
        if concurrency is None:
            concurrency = self.protocol.concurrency

        if timeout is None:
            timeout = self.protocol.timeouts.total_timeout

        return [ asyncio.create_task(
            self.execute_prepared_request(request.name, idx, timeout)
        ) for idx in range(concurrency)]
