from typing import List
from hedra.reporting.events.types.base_event import BaseEvent
from hedra.reporting.metric import Metric


try:
    from motor.motor_asyncio import AsyncIOMotorClient
    from .mongodb_config import MongoDBConfig
    has_connector = True

except Exception:
    AsyncIOMotorClient = None
    MongoDBConfig = None
    has_connector = False



class MongoDB:

    def __init__(self, config: MongoDBConfig) -> None:
        self.host = config.host
        self.username = config.username
        self.password = config.password
        self.database_name = config.database
        self.events_collection = config.events_collection
        self.metrics_collection = config.metrics_collection

        self.connection: AsyncIOMotorClient = None
        self.database = None

    async def connect(self):
        if self.username and self.password:
            connection_string = f'mongodb://{self.username}:{self.password}@{self.host}/{self.database_name}'
        
        else:
            connection_string = f'mongodb://{self.host}/{self.database_name}'

        self.connection = AsyncIOMotorClient(connection_string)
        self.database = self.connection[self.database_name]

    async def submit_events(self, events: List[BaseEvent]): 
        await self.database[self.events_collection].insert_many(
            [event.record for event in events]
        )

    async def submit_metrics(self, metrics: List[Metric]):
        await self.database[self.metrics_collection].insert_many(
            [metric.record for metric in metrics]
        )

    async def close(self):
        pass