from typing import List
from hedra.reporting.events.types.base_event import BaseEvent
from hedra.reporting.metric import MetricsGroup


try:
    import sqlalchemy
    from sqlalchemy.schema import CreateTable
    from sqlalchemy.ext.asyncio import create_async_engine
    from .sqlite_config import SQLiteConfig
    has_connector = True

except Exception:
    ASYNCIO_STRATEGY = None
    sqlalchemy = None
    SQLiteConfig = None
    CreateTable = None
    OperationalError = None
    has_connector = False



class SQLite:

    def __init__(self, config: SQLiteConfig) -> None:
        self.path = f'sqlite+aiosqlite:///{config.path}'
        self.events_table_name = config.events_table
        self.metrics_table_name = config.metrics_table
        self.group_metrics_table_name = f'{self.metrics_table_name}_group_metrics'
        self.errors_table_name = f'{self.metrics_table_name}_errors'
        self.custom_fields = config.custom_fields
        self.metadata = sqlalchemy.MetaData()
        self.database = None
        self._engine = None
        self._connection = None
        self._events_table = None
        self._metrics_table = None
        self._group_metrics_table = None
        self._errors_table = None

    async def connect(self):
        self._engine = create_async_engine(self.path)
    
    async def submit_events(self, events: List[BaseEvent]):

        async with self._engine.begin() as connection:
            for event in events:

                if self._events_table is None:

                    events_table = sqlalchemy.Table(
                        self.events_table_name,
                        self.metadata,
                        sqlalchemy.Column('id', sqlalchemy.INTEGER, primary_key=True,),
                        sqlalchemy.Column('name', sqlalchemy.TEXT),
                        sqlalchemy.Column('stage', sqlalchemy.TEXT),
                        sqlalchemy.Column('time', sqlalchemy.REAL),
                        sqlalchemy.Column('succeeded', sqlalchemy.INTEGER)
                    )

                    
                    await connection.execute(CreateTable(events_table, if_not_exists=True))
                    self._events_table = events_table
            
                await connection.execute(self._events_table.insert(values=event.record))
            
            await connection.commit()

    async def submit_common(self, metrics_groups: List[MetricsGroup]):

        async with self._engine.begin() as connection:
            if self._group_metrics_table is None:

                group_metrics_table = sqlalchemy.Table(
                    self.group_metrics_table_name,
                    self.metadata,
                    sqlalchemy.Column('id', sqlalchemy.INTEGER, primary_key=True),
                    sqlalchemy.Column('name', sqlalchemy.TEXT),
                    sqlalchemy.Column('stage', sqlalchemy.TEXT),
                    sqlalchemy.Column('total', sqlalchemy.INTEGER),
                    sqlalchemy.Column('succeeded', sqlalchemy.INTEGER),
                    sqlalchemy.Column('failed', sqlalchemy.INTEGER),
                )

                await connection.execute(CreateTable(group_metrics_table, if_not_exists=True))
                self._group_metrics_table = group_metrics_table

            for metrics_group in metrics_groups:
                await connection.execute(self._metrics_table.insert(values={
                    'name': metrics_group.name,
                    'stage': metrics_group.stage,
                    **metrics_group.common_stats
                }))

    async def submit_metrics(self, metrics: List[MetricsGroup]):
        async with self._engine.begin() as connection:

            for metrics_group in metrics:

                if self._metrics_table is None:

                    metrics_table = sqlalchemy.Table(
                        self.metrics_table_name,
                        self.metadata,
                        sqlalchemy.Column('id', sqlalchemy.INTEGER, primary_key=True),
                        sqlalchemy.Column('name', sqlalchemy.TEXT),
                        sqlalchemy.Column('stage', sqlalchemy.TEXT),
                        sqlalchemy.Column('group', sqlalchemy.TEXT),
                        sqlalchemy.Column('median', sqlalchemy.REAL),
                        sqlalchemy.Column('mean', sqlalchemy.REAL),
                        sqlalchemy.Column('variance', sqlalchemy.REAL),
                        sqlalchemy.Column('stdev', sqlalchemy.REAL),
                        sqlalchemy.Column('minimum', sqlalchemy.REAL),
                        sqlalchemy.Column('maximum', sqlalchemy.REAL)
                    )

                    for quantile in metrics_group.quantiles:
                        metrics_table.append_column(
                            sqlalchemy.Column(f'{quantile}', sqlalchemy.REAL)
                        )

                    for custom_field_name, sql_alchemy_type in metrics_group.custom_schemas:
                        metrics_table.append_column(custom_field_name, sql_alchemy_type)   
                    
                    await connection.execute(CreateTable(metrics_table, if_not_exists=True))
                    self._metrics_table = metrics_table

                for group_name, group in metrics_group.groups.items():
                    await connection.execute(self._metrics_table.insert(values={
                        **group.record,
                        'group': group_name
                    }))



    async def submit_errors(self, metrics_groups: List[MetricsGroup]):

        async with self._engine.begin() as connection:
            for metrics_group in metrics_groups:

                if self._errors_table is None:

                    metrics_errors_table = sqlalchemy.Table(
                        f'{self.metrics_table_name}_errors',
                        self.metadata,
                        sqlalchemy.Column('id', sqlalchemy.INTEGER, primary_key=True),
                        sqlalchemy.Column('metric_name', sqlalchemy.TEXT),
                        sqlalchemy.Column('metrics_stage', sqlalchemy.TEXT),
                        sqlalchemy.Column('error_message', sqlalchemy.TEXT),
                        sqlalchemy.Column('error_count', sqlalchemy.INTEGER)
                    ) 

                    await connection.execute(CreateTable(metrics_errors_table, if_not_exists=True))

                    self._errors_table = metrics_errors_table

                for error in metrics_group.errors:
                    await connection.execute(
                        self._errors_table.insert(values={
                            'metric_name': metrics_group.name,
                            'metric_stage': metrics_group.stage,
                            'error_message': error.get('message'),
                            'error_count': error.get('count')
                        })
                    )

            await connection.commit()

    async def close(self):
        pass