import uuid
from typing import Any, List

from matplotlib.pyplot import get
from hedra.reporting.events.types.base_event import BaseEvent
from hedra.reporting.metric import MetricsGroup


try:
    from azure.cosmos.aio import CosmosClient
    from azure.cosmos import PartitionKey
    from .cosmosdb_config import CosmosDBConfig
    has_connector = True
except Exception:
    CosmosClient = None
    PartitionKey = None
    CosmosDBConfig = None
    has_connector = False


class CosmosDB:

    def __init__(self, config: CosmosDBConfig) -> None:
        self.account_uri = config.account_uri
        self.account_key = config.account_key
        self.database_name = config.database
        self.events_container_name = config.events_container
        self.metrics_container_name = config.metrics_container
        self.group_metrics_container_name = f'{self.metrics_container_name}_group_metrics'
        self.errors_container_name = f'{self.metrics_container_name}_errors'
        self.events_partition_key = config.events_partition_key
        self.metrics_partition_key = config.metrics_partition_key
        self.group_metrics_partition_key = f'{self.metrics_partition_key}_group_metrics'
        self.errors_partition_key = f'{self.metrics_partition_key}_errors'
        self.analytics_ttl = config.analytics_ttl

        self.events_container = None
        self.metrics_container = None
        self.group_metrics_container = None
        self.errors_container = None
        self.client = None
        self.database = None

    async def connect(self):
        self.client = CosmosClient(
            self.account_uri,
            credential=self.account_key
        )

        self.database = await self.client.create_database_if_not_exists(self.database_name)

    async def submit_events(self, events: List[BaseEvent]):

        self.events_container = await self.database.create_container_if_not_exists(
            self.events_container_name,
            PartitionKey(f'/{self.events_partition_key}')
        )

        for event in events:
            await self.events_container.upsert_item({
                'id': str(uuid.uuid4()),
                **event.record
            })

    async def submit_common(self, metrics_groups: List[MetricsGroup]):
        self.group_metrics_container = await self.database.create_container_if_not_exists(
            self.group_metrics_container_name,
            PartitionKey(f'/{self.group_metrics_partition_key}')
        )

        for metrics_group in metrics_groups:
            await self.group_metrics_container.upsert_item({
                'id': str(uuid.uuid4()),
                'name': metrics_group.name,
                'stage': metrics_group.stage,
                **metrics_group.common_stats
            })
        
    async def submit_metrics(self, metrics: List[MetricsGroup]):

        self.metrics_container = await self.database.create_container_if_not_exists(
            self.metrics_container_name,
            PartitionKey(f'/{self.metrics_partition_key}')
        )

        for metrics_group in metrics:
            for group_name, group in metrics_group.groups.items():
                await self.metrics_container.upsert_item({
                    'id': str(uuid.uuid4()),
                    'group': group_name,
                    **group.record
                })

    async def submit_errors(self, metrics_groups: List[MetricsGroup]):
        self.errors_container = await self.database.create_container_if_not_exists(
            self.errors_container_name,
            PartitionKey(f'/{self.errors_partition_key}')
        )

        for metrics_group in metrics_groups:
            for error in metrics_group.errors:
                await self.metrics_container.upsert_item({
                    'id': str(uuid.uuid4()),
                    'metric_name': metrics_group.name,
                    'metrics_stage': metrics_group.stage,
                    'error_message': error.get('message'),
                    'error_count': error.get('count')
                })

    async def close(self):
        await self.client.close()
        