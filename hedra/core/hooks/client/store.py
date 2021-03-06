import asyncio
from collections import defaultdict
from typing import Any


class ActionsStore:

    def __init__(self) -> None:
        self.actions = defaultdict(dict)
        self.sessions = defaultdict(dict)
        self._loop = None
        self.current_stage: str = None
        self.waiter = None

    def set_waiter(self, stage: str):

        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        self.waiter = self._loop.create_future()
        self.current_stage = stage

    async def wait_for_ready(self):
        await self.waiter

    def store(self, request: str, action: Any, session: Any):

        self.actions[self.current_stage][request] = action
        self.sessions[self.current_stage][request] = session

        try:
            self.waiter.set_result(None)
        except asyncio.exceptions.CancelledError:
            pass

    def get(self, stage: str, action_name: str):
        action = self.actions.get(
            stage
        ).get(action_name)

        session = self.sessions.get(
            stage
        ).get(action_name)

        return action, session
