"""Generated from Smithy shape ``com.amazonaws.iot#InfluxDBBatchConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.influx_db_batch_across_topics
    import capo_iot.types.influx_db_max_batch_open_ms
    import capo_iot.types.influx_db_max_batch_size
    import capo_iot.types.influx_db_max_batch_size_bytes


class InfluxDBBatchConfig(TypedDict, closed=True):
    max_batch_size: NotRequired[
        "capo_iot.types.influx_db_max_batch_size.InfluxDBMaxBatchSize"
    ]
    """<p>The maximum number of data points to collect in a batch.</p> <p>If you don't specify a value, this limit doesn't apply. IoT then closes each batch when another configured limit is reached.</p>"""
    max_batch_open_ms: NotRequired[
        "capo_iot.types.influx_db_max_batch_open_ms.InfluxDBMaxBatchOpenMs"
    ]
    """<p>The maximum length of time, in milliseconds, to keep a batch open before writing it to InfluxDB.</p> <p>If you don't specify a value, this limit doesn't apply. IoT then closes each batch when another configured limit is reached.</p>"""
    max_batch_size_bytes: NotRequired[
        "capo_iot.types.influx_db_max_batch_size_bytes.InfluxDBMaxBatchSizeBytes"
    ]
    """<p>The maximum size of a batch, in bytes, before IoT writes it to InfluxDB.</p> <p>If you don't specify a value, this limit doesn't apply. IoT then closes each batch when another configured limit is reached.</p>"""
    batch_across_topics: (
        "capo_iot.types.influx_db_batch_across_topics.InfluxDBBatchAcrossTopics"
    )
    """<p>Specifies whether to collect data points from different topics into the same batch.</p> <p>If omitted or <code>false</code>, IoT batches data points for each topic separately.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InfluxDBBatchConfig) -> dict:
    out: dict = {}
    if "max_batch_size" in value:
        out["maxBatchSize"] = value["max_batch_size"]
    if "max_batch_open_ms" in value:
        out["maxBatchOpenMs"] = value["max_batch_open_ms"]
    if "max_batch_size_bytes" in value:
        out["maxBatchSizeBytes"] = value["max_batch_size_bytes"]
    out["batchAcrossTopics"] = value.get("batch_across_topics", False)
    return out


def deserialize_json(data: dict) -> InfluxDBBatchConfig:
    out: InfluxDBBatchConfig = {}  # type: ignore[typeddict-item]
    if data.get("maxBatchSize") is not None:
        out["max_batch_size"] = data["maxBatchSize"]
    if data.get("maxBatchOpenMs") is not None:
        out["max_batch_open_ms"] = data["maxBatchOpenMs"]
    if data.get("maxBatchSizeBytes") is not None:
        out["max_batch_size_bytes"] = data["maxBatchSizeBytes"]
    if data.get("batchAcrossTopics") is not None:
        out["batch_across_topics"] = data["batchAcrossTopics"]
    else:
        out["batch_across_topics"] = False
    return out
