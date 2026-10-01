"""Generated from Smithy shape ``com.amazonaws.kafka#PartitionStrategy``."""

from typing import Literal, TypeAlias, cast

"""<p>The partitioning strategy used to partition records in the destination Apache Iceberg table.</p>"""
PartitionStrategy: TypeAlias = Literal["TIME_HOUR",]


# --- restJson1 ser/de ---
def serialize_json(value: PartitionStrategy) -> str:
    return value


def deserialize_json(data: str) -> PartitionStrategy:
    return cast(PartitionStrategy, data)
