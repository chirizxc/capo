"""Generated from Smithy shape ``com.amazonaws.glue#ConnectionStringToStringMap``."""

from typing import TypeAlias

ConnectionStringToStringMap: TypeAlias = dict["str", "str"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ConnectionStringToStringMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionStringToStringMap:
    out: ConnectionStringToStringMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
