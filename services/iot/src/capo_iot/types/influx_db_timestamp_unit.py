"""Generated from Smithy shape ``com.amazonaws.iot#InfluxDBTimestampUnit``."""

from typing import Literal, TypeAlias, cast

InfluxDBTimestampUnit: TypeAlias = Literal[
    "s",
    "ms",
    "us",
    "ns",
]


# --- restJson1 ser/de ---
def serialize_json(value: InfluxDBTimestampUnit) -> str:
    return value


def deserialize_json(data: str) -> InfluxDBTimestampUnit:
    return cast(InfluxDBTimestampUnit, data)
