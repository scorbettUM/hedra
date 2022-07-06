import random
import time
import asyncio
from typing import List
from async_tools.datatypes.async_list import AsyncList
from async_tools.functions import awaitable
from hedra.core.engines import Engine
from hedra.core.personas.types.default_persona import DefaultPersona
from hedra.core.parsing import ActionsParser
from hedra.test.actions.base import Action


class WeightedSelectionPersona(DefaultPersona):

    def __init__(self, config=None, handler=None):
        super().__init__(config=config, handler=handler)
        self.weights = []
        self.sampled_actions: List[Action] = []
        
    @classmethod
    def about(cls):
        return '''
        Weighted Persona - (sequence)

        Executes batches of actions of the batch size specified by the --batch-size  argument. Actions for each batch are resampled each iteration according 
        to their specified "weight". As with other personas, the Weighted persona will execute for the total amount of time specified by the --total-time 
        argument. You may specify a wait between batches (between each step) by specifying an integer number of seconds via the --batch-interval argument.
        '''

    async def setup(self, parser: ActionsParser):

        self.session_logger.debug('Setting up persona...')

        self.actions = parser.actions

        for action_set in self.actions.values():
            self.actions_count += action_set.registry.count
            await action_set.setup()

            self._parsed_actions.extend(
                action_set.registry.to_list()
            )

        self.sampled_actions = self._sample()
        self.duration = self.total_time

    async def execute(self):
        elapsed = 0
        results = []

        await self.start_updates()

        self.start = time.time()

        while elapsed < self.total_time:

            next_timeout = self.total_time - elapsed
            action = self.sampled_actions.pop()

            if action.before_batch:
                action = await action.before_batch(action)
            
            self.batch.deferred.append(asyncio.create_task(
                action.session.batch_request(
                    action.parsed,
                    concurrency=self.batch.size,
                    timeout=next_timeout
                )
            ))
            
            await asyncio.sleep(self.batch.interval.period)

            if action.after_batch:
                action = await action.after_batch(action)

            elapsed = time.time() - self.start

            if len(self.sampled_actions) < 1:
                self.sampled_actions = self._sample()

        self.end = elapsed + self.start

        await self.stop_updates()

        for deferred_batch in self.batch.deferred:
            batch, pending = await deferred_batch
            completed = await asyncio.gather(*batch, return_exceptions=True)
            results.extend(completed)

            try:
                for pend in pending:
                    pend.cancel()
            except Exception:
                pass

        self.total_actions = len(results)
        self.total_elapsed = elapsed

        return results

    def _sample(self) -> List[Action]:
        return random.choices(
            self._parsed_actions.data,
            self.weights,
            k=self.actions_count
        )
