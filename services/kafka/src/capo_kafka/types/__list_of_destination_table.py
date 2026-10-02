"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfDestinationTable``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kafka.types.destination_table

__listOfDestinationTable: TypeAlias = list[
    "capo_kafka.types.destination_table.DestinationTable"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDestinationTable) -> list:
    import capo_kafka.types.destination_table

    out: list = []
    for item in value:
        out.append(capo_kafka.types.destination_table.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfDestinationTable:
    import capo_kafka.types.destination_table

    out: __listOfDestinationTable = []
    for item in data:
        if item is None:
            continue
        out.append(capo_kafka.types.destination_table.deserialize_json(item))
    return out
