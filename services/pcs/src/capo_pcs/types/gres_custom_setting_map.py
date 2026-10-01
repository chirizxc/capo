"""Generated from Smithy shape ``com.amazonaws.pcs#GresCustomSettingMap``."""

from typing import TypeAlias

GresCustomSettingMap: TypeAlias = dict["str", "str"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: GresCustomSettingMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> GresCustomSettingMap:
    out: GresCustomSettingMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
