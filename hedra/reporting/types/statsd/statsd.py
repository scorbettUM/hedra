import re
from typing import List
from hedra.reporting.events.types.base_event import BaseEvent
from hedra.reporting.metric import MetricsGroup


try:
    from aio_statsd import StatsdClient
    from .statsd_config import StatsDConfig
    has_connector = True

except Exception:
    StatsdClient = None
    StatsDConfig = None
    has_connector = False


class StatsD:

    def __init__(self, config: StatsDConfig) -> None:
        self.host = config.host
        self.port = config.port

        self.connection = StatsdClient(
            host=self.host,
            port=self.port
        )

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
            'quantiles': 'gauge'
        }

        self._update_map = {
            'count': self.connection.counter,
            'gauge': self.connection.gauge,
            'increment': self.connection.increment,
            'sets': self.connection.sets,
            'histogram': lambda: NotImplementedError('StatsD does not support histograms.'),
            'distribution': lambda: NotImplementedError('StatsD does not support distributions.'),
            'timer': self.connection.timer

        }

    async def connect(self):
        await self.connection.connect()

    async def submit_events(self, events: List[BaseEvent]):

        for event in events:
            time_update_function = self._update_map.get('gauge')
            time_update_function(f'{event.name}_time', event.time)
            
            if event.success:
                success_update_function = self._update_map.get('count')
                success_update_function(f'{event.name}_success', 1)
            
            else:
                failed_update_function = self._update_map.get('count')
                failed_update_function(f'{event.name}_failed', 1)

    async def submit_common(self, metrics_groups: List[MetricsGroup]):

        for metrics_group in metrics_groups:
            
            for field, value in metrics_group.common_stats.items():
                update_type = self.types_map.get(field)
                update_function = self._update_map.get(update_type)

                update_function(
                    f'{metrics_group.name}_{field}', value
                )

    async def submit_metrics(self, metrics: List[MetricsGroup]):

        for metrics_group in metrics:

            for group_name, group in metrics_group.groups.items():

                metric_record = {**group.stats, **group.custom}
                metric_types = {**self.types_map, **group.custom_schemas}

                for metric_field, metric_value in metric_record.items():
                    update_type = metric_types.get(metric_field)
                    update_function = self._update_map.get(update_type)
                    
                    update_function(
                        f'{metrics_group.name}_{group_name}_{metric_field}', metric_value
                    )

    async def submit_errors(self, metrics_groups: List[MetricsGroup]):

        for metrics_group in metrics_groups:
            for error in metrics_group.errors:
                error_message = re.sub(
                    '[^0-9a-zA-Z]+', 
                    '_',
                    error.get(
                        'message'
                    ).lower()
                )

                update_function = self._update_map.get('count')
                update_function(f'{metrics_group.name}_{error_message}', error.get('count'))


    async def close(self):
        await self.connection.close()