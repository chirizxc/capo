"""Generated from Smithy shape ``com.amazonaws.iot#InfluxDBTagMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.influx_db_tag_name
    import capo_iot.types.influx_db_tag_value

InfluxDBTagMap: TypeAlias = dict[
    "capo_iot.types.influx_db_tag_name.InfluxDBTagName",
    "capo_iot.types.influx_db_tag_value.InfluxDBTagValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: InfluxDBTagMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> InfluxDBTagMap:
    out: InfluxDBTagMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
