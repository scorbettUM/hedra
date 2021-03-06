from typing import Dict
from hedra.core.hooks.types.types import HookType
from hedra.core.pipelines.stages.types.stage_types import StageTypes
from hedra.reporting import (
    Reporter,
    BigQueryConfig,
    BigTableConfig,
    CassandraConfig,
    CloudwatchConfig,
    CosmosDBConfig,
    CSVConfig,
    DatadogConfig,
    DogStatsDConfig,
    GoogleCloudStorageConfig,
    GraphiteConfig,
    HoneycombConfig,
    InfluxDBConfig,
    JSONConfig,
    KafkaConfig,
    MongoDBConfig,
    MySQLConfig,
    NetdataConfig,
    NewRelicConfig,
    PostgresConfig,
    PrometheusConfig,
    RedisConfig,
    S3Config,
    SnowflakeConfig,
    SQLiteConfig,
    StatsDConfig,
    TelegrafConfig,
    TelegrafStatsDConfig,
    TimescaleDBConfig
)
from .stage import Stage


class Submit(Stage):
    stage_type=StageTypes.SUBMIT
    config: (
        BigQueryConfig | BigTableConfig | CassandraConfig | CloudwatchConfig | CosmosDBConfig |
        CSVConfig | DatadogConfig | DogStatsDConfig | GoogleCloudStorageConfig | GraphiteConfig | HoneycombConfig |
        InfluxDBConfig | JSONConfig | KafkaConfig | MongoDBConfig | MySQLConfig | NetdataConfig |
        NewRelicConfig | PostgresConfig | PrometheusConfig | RedisConfig | S3Config | SnowflakeConfig |
        SQLiteConfig | StatsDConfig | TelegrafConfig | TelegrafStatsDConfig | TimescaleDBConfig
    ) = None
    submit_events: bool = False
    
    def __init__(self) -> None:
        super().__init__()
        self.summaries = {}
        self.events = []
        self.reporter = Reporter(self.config)
        self.hooks: Dict[str, HookType] = {}

        for hook_type in HookType:
            self.hooks[hook_type] = []

    async def run(self):
        await self.reporter.connect()

        if self.submit_events:
            await self.reporter.submit_events(self.events)

        metrics = []

        stage_summaries = self.summaries.get('stages', {})
        for stage in stage_summaries.values():

            metrics.extend(list(
                stage.get('actions', {}).values()
            ))

        await self.reporter.submit_common(metrics)
        await self.reporter.submit_metrics(metrics)
        await self.reporter.submit_errors(metrics)
        await self.reporter.close()

