import inspect
from types import FunctionType
from typing import Any, Dict, List
from hedra.core.hooks.client.config import Config
from hedra.core.engines.types.common import Request
from hedra.core.engines.types.common.hooks import Hooks
from hedra.core.engines.types.common.types import RequestTypes
from hedra.core.engines.types.grpc.client import MercuryGRPCClient
from hedra.core.engines.types.common import Timeouts
from .base_client import BaseClient


class GRPCClient(BaseClient):
    
    def __init__(self, config: Config) -> None:
        super().__init__()

        self.session = MercuryGRPCClient(
            concurrency=config.batch_size,
            timeouts=Timeouts(
                total_timeout=config.request_timeout
            ),
            reset_connections=config.options.get('reset_connections')
        )
        self.request_type = RequestTypes.GRPC
        self.next_name = None

    def __getitem__(self, key: str):
        return self.session.registered.get(key)

    async def request(
        self, 
        url: str, 
        headers: Dict[str, str] = {}, 
        protobuf: Any = None, 
        user: str = None, 
        tags: List[Dict[str, str]] = [], 
        checks: List[FunctionType]=[]
    ):
        if self.session.registered.get(self.next_name) is None:
            result = await self.session.prepare(
                Request(
                    self.next_name,
                    url,
                    method='POST',
                    headers=headers,
                    payload=protobuf,
                    user=user,
                    tags=tags,
                    checks=checks,
                    request_type=self.request_type
                )
            )

            if isinstance(result, Exception):
                raise result

        return self.session