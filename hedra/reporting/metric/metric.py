from typing import Any, Dict, List, Union
from hedra.reporting.tags import Tag


class Metric:

    def __init__(
        self,
        name: str,
        source: str,
        stage: str, 
        data: Dict[str, Union[int, float, str, bool]], 
        tags: Dict[str, str]
    ) -> None:
        self.name = name
        self.stage = stage
        self.data = []

        self.fields = [
            'name',
            'stage'
        ]
        self.values = [
            name,
            stage
        ]

        self._additional_fields = ["quantiles", "errors", "custom_fields"]
        self.source = source
        self._raw_data = data
        self.tags = [
            Tag(tag_name, tag_value) for tag_name, tag_value in tags.items()
        ]

        flattened_data = dict({
            field: value for field, value in data.items() if field not in self._additional_fields
        })
  
        for metric_name, metric_value in flattened_data.items():
            self.data.append((
                metric_name,
                metric_value
            ))

            self.fields.append(metric_name)
            self.values.append(metric_value)

        for quantile, quantile_value in data.get("quantiles", {}).items():
            self.data.append((
                quantile,
                quantile_value
            ))

            self.fields.append(quantile)
            self.values.append(quantile_value)

        self.errors: List[Dict[str, Union[str, int]]] = data.get('errors')
        self.custom_fields: Dict[str, Dict[str, Union[int, float, Any]]] = None

    @property
    def custom(self):
        return {
            custom_metric_name: custom_metric.get(
                'result'
            ) for custom_metric_name, custom_metric in self.custom_fields.items()
        }

    @property
    def custom_schemas(self):
        return {
            custom_metric_name: custom_metric.get(
                'field_type'
            ) for custom_metric_name, custom_metric in self.custom_fields.items()
        }

    @property
    def custom_field_names(self):
        return list(self.custom_fields.keys())

    @property
    def record(self):

        record_data = {
            f'{field}': value for field, value in self.data
        }

        custom_field_data = {
            f'{field}': value for field, value in self.custom.items()
        }

        return {
            'name': self.name,
            'stage': self.stage,
            **record_data,
            **custom_field_data
        }

    @property
    def raw_data(self):
        return self._raw_data

    @property
    def stats(self):
        stats_metrics = {}
        for metric_name, metric_value in self.data:
            if isinstance(metric_value, (int, float)):
                stats_metrics[metric_name] = metric_value

        return stats_metrics

    @property
    def quantiles(self):
        return self._raw_data.get('quantiles', {})