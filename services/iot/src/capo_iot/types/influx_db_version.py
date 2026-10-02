"""Generated from Smithy shape ``com.amazonaws.iot#InfluxDBVersion``."""

from typing import Literal, TypeAlias, cast

InfluxDBVersion: TypeAlias = Literal[
    "V2",
    "V3",
]


# --- restJson1 ser/de ---
def serialize_json(value: InfluxDBVersion) -> str:
    return value


def deserialize_json(data: str) -> InfluxDBVersion:
    return cast(InfluxDBVersion, data)
