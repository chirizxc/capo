"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfPartitionSource``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kafka.types.partition_source

__listOfPartitionSource: TypeAlias = list[
    "capo_kafka.types.partition_source.PartitionSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfPartitionSource) -> list:
    import capo_kafka.types.partition_source

    out: list = []
    for item in value:
        out.append(capo_kafka.types.partition_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfPartitionSource:
    import capo_kafka.types.partition_source

    out: __listOfPartitionSource = []
    for item in data:
        if item is None:
            continue
        out.append(capo_kafka.types.partition_source.deserialize_json(item))
    return out
