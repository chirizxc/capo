"""Generated from Smithy shape ``com.amazonaws.kafka#PartitionSpec``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__list_of_partition_source
    import capo_kafka.types.partition_strategy


class PartitionSpec(TypedDict, closed=True):
    partition_strategy: NotRequired[
        "capo_kafka.types.partition_strategy.PartitionStrategy"
    ]
    """<p>The partitioning strategy applied to records written to the table.</p>"""
    source_list: NotRequired[
        "capo_kafka.types.__list_of_partition_source.__listOfPartitionSource"
    ]
    """<p>The source columns used by the partitioning strategy. For TIME_HOUR, must contain exactly one source column whose value is a timestamp.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PartitionSpec) -> dict:
    out: dict = {}
    if "partition_strategy" in value:
        import capo_kafka.types.partition_strategy

        out["partitionStrategy"] = capo_kafka.types.partition_strategy.serialize_json(
            value["partition_strategy"]
        )
    if "source_list" in value:
        import capo_kafka.types.__list_of_partition_source

        out["sourceList"] = capo_kafka.types.__list_of_partition_source.serialize_json(
            value["source_list"]
        )
    return out


def deserialize_json(data: dict) -> PartitionSpec:
    out: PartitionSpec = {}  # type: ignore[typeddict-item]
    if data.get("partitionStrategy") is not None:
        import capo_kafka.types.partition_strategy

        out["partition_strategy"] = (
            capo_kafka.types.partition_strategy.deserialize_json(
                data["partitionStrategy"]
            )
        )
    if data.get("sourceList") is not None:
        import capo_kafka.types.__list_of_partition_source

        out["source_list"] = (
            capo_kafka.types.__list_of_partition_source.deserialize_json(
                data["sourceList"]
            )
        )
    return out
