import asyncio
import functools
from re import S
import re
from hedra.reporting.events.types.base_event import BaseEvent
from hedra.reporting.metric.metrics_group import MetricsGroup

try:
    # Datadog uses aiosonic
    from aiosonic import HTTPClient, TCPConnector, Timeouts
    from datadog_api_client import (
        AsyncApiClient, 
        Configuration
    )
    from datadog_api_client.v2.api.metrics_api import (MetricsApi, MetricPayload)
    from datadog_api_client.v2.model.metric_series import MetricSeries
    from datadog_api_client.v2.model.metric_point import MetricPoint

    from datadog_api_client.v1.api.events_api import EventsApi
    from datadog_api_client.v1.api.events_api import EventCreateRequest
    from .datadog_config import DatadogConfig
    has_connector = True

except Exception:
    datadog = None
    DatadogConfig = None
    has_connector = False

from datetime import datetime
from typing import Any, List


class Datadog:

    def __init__(self, config: DatadogConfig) -> None:
        self.datadog_api_key = config.api_key
        self.datadog_app_key = config.app_key
        self.event_alert_type = config.event_alert_type or 'info'
        self.device_name = config.device_name or 'hedra'
        self.priority = config.priority
        self.custom_fields = config.custom_fields or {}

        self.types_map = {
            'total': 'count',
            'succeeded': 'count',
            'failed': 'count',
            'median': 'gauge',
            'mean': 'gauge',
            'variance': 'gauge',
            'stdev': 'gauge',
            'minimum': 'gauge',
            'maximum': 'gauge',
            **self.custom_fields
        }
        
        self._datadog_api_map = {
            'count': 1,
            'rate': 2,
            'gauge': 3
        }

        self._config = None
        self._client = None
        self.events_api = None
        self.metrics_api = None

    async def connect(self):
        self._config = Configuration()
        self._config.api_key["apiKeyAuth"] = self.datadog_api_key
        self._config.api_key["appKeyAuth"] = self.datadog_app_key

        self._client = AsyncApiClient(self._config)

        # Datadog's implementation of aiosonic's HTTPClient lacks a lot
        # of configurability, incuding actually being able to set request timeouts
        # so we substitute our own implementation.

        tcp_connection = TCPConnector(timeouts=Timeouts(sock_connect=30))
        self._client.rest_client._client = HTTPClient(tcp_connection)

        self.events_api = EventsApi(self._client)
        self.metrics_api = MetricsApi(self._client)


    async def submit_events(self, events: List[BaseEvent]):

        for event in events:

            tags = {
                f'{tag.name}:{tag.value}' for tag in event.tags
            }

            await self.events_api.create_event(
                EventCreateRequest(
                    title=event.name,
                    text=event.serialize(),
                    alert_type=self.event_alert_type,
                    aggregation_key=event.type,
                    device_name=self.device_name,
                    date_happened=datetime.now().strftime('%Y-%m-%dT%H:%M:%S.Z'),
                    priority=self.priority,
                    tags=tags,
                    host=event.hostname
                )
            )

    async def submit_common(self, metrics_groups: List[MetricsGroup]):

        metrics_series = []
        for metrics_group in metrics_groups:
            tags = [
                f'{tag.name}:{tag.value}' for tag in metrics_group.tags
            ]

            for field, value in metrics_group.common_stats.items():
                metric_type = self.types_map.get(field)
                datadog_metric_type = self._datadog_api_map.get(metric_type)

                series = MetricSeries(
                    f'{metrics_group.name}_{field}', 
                    [MetricPoint(
                        timestamp=int(datetime.now().timestamp()),
                        value=float(value)
                    )],
                    type=datadog_metric_type,
                    tags=[
                        *tags,
                        f'metric_stage:{metrics_group.stage}',
                        f'group:common'
                    ]
                )

                metrics_series.append(series)
                
        await self.metrics_api.submit_metrics(MetricPayload(metrics_series))        

    async def submit_metrics(self, metrics: List[MetricsGroup]):

        for metrics_group in metrics:

            tags = [
                f'{tag.name}:{tag.value}' for tag in metrics_group.tags
            ]

            metrics_series = []
            for group_name, group in metrics_group.groups.items():
                for field, value in group.stats.items():
                    metric_type = self.types_map.get(field)
                    datadog_metric_type = self._datadog_api_map.get(metric_type)

                    series = MetricSeries(
                        f'{metrics_group.name}_{field}', 
                        [MetricPoint(
                            timestamp=int(datetime.now().timestamp()),
                            value=float(value)
                        )],
                        type=datadog_metric_type,
                        tags=[
                            *tags,
                            f'metric_stage:{metrics_group.stage}',
                            f'group:{group_name}'
                        ]
                    )

                    metrics_series.append(series)

                for quantile_name, quantile_value in group.quantiles.items():
                    datadog_metric_type = self._datadog_api_map.get('gauge')
                    series = MetricSeries(
                        f'{metrics_group.name}_{quantile_name}', 
                        [MetricPoint(
                            timestamp=int(datetime.now().timestamp()),
                            value=float(quantile_value)
                        )],
                        type=datadog_metric_type,
                        tags=[
                            *tags,
                            f'metric_stage:{metrics_group.stage}',
                            f'group:{group_name}'
                        ]
                    )

                    metrics_series.append(series)
     
                for custom_field_name, value in group.custom.items():
                    datadog_metric_type = group.custom_schemas.get(custom_field_name)
                    datadog_type = self._datadog_api_map.get(datadog_metric_type)

                    series = MetricSeries(
                        f'{metrics_group.name}_{custom_field_name}', 
                        [MetricPoint(
                            timestamp=int(datetime.now().timestamp()),
                            value=float(value)
                        )],
                        type=datadog_type,
                        tags=[
                            *tags,
                            f'metric_stage:{metrics_group.stage}',
                            f'group:{group_name}'
                        ]
                    )

                    metrics_series.append(series)
            
            await self.metrics_api.submit_metrics(MetricPayload(metrics_series))

    async def submit_events(self, metrics_groups: List[MetricsGroup]):

        for metrics_group in metrics_groups:
            error_series = [] 

            for error in metrics_group.errors:
                
            
                error_message = error.get('error_message')

                series = MetricSeries(
                    f'{metrics_group.name}_errors',
                    [MetricPoint(
                        timestamp=int(datetime.now().timestamp()),
                        value=float(error.get('count'))
                    )],
                    type=self._datadog_api_map.get('count'),
                    tags=[
                        f'metric_stage:{metrics_group.stage}',
                        f'error_message:{error_message}'
                    ]
                )
               
                error_series.append(series)

            await self.metrics_api.submit_metrics(MetricPayload(error_series))

    async def close(self):
        pass
