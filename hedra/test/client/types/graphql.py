import inspect
from types import FunctionType
from typing import Any, Dict, List
from hedra.core.engines.types.common import Request
from hedra.core.engines.types.graphql.client import MercuryGraphQLClient
from hedra.core.engines.types.common.types import RequestTypes


class GraphQLClient:

    def __init__(self, session: MercuryGraphQLClient) -> None:
        self.session = session
        self.request_type = RequestTypes.GRAPHQL

    def __getitem__(self, key: str):
        return self.session.registered.get(key)

    async def query(
        self,
        url: str, 
        query: str,
        operation_name: str = None,
        variables: Dict[str, Any] = None, 
        headers: Dict[str, str] = {}, 
        user: str = None, 
        tags: List[Dict[str, str]] = [], 
        checks: List[FunctionType]=[]
    ):
        if self.session.protocol.registered.get(self.next_name) is None:
            result = await self.session.prepare(
                Request(
                    callable,
                    url,
                    method='POST',
                    headers=headers,
                    payload={
                        "query": query,
                        "operation_name": operation_name,
                        "variables": variables
                    },
                    user=user,
                    tags=tags,
                    checks=checks,
                    request_type=self.request_type
                )
            )

            if result and result.error:
                raise result.error