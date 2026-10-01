"""Generated from Smithy shape ``com.amazonaws.devicefarm#InsightsTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_device_farm.types.insights_type

InsightsTypes: TypeAlias = list["capo_device_farm.types.insights_type.InsightsType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InsightsTypes) -> list:
    import capo_device_farm.types.insights_type

    out: list = []
    for item in value:
        out.append(capo_device_farm.types.insights_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InsightsTypes:
    import capo_device_farm.types.insights_type

    out: InsightsTypes = []
    for item in data:
        if item is None:
            continue
        out.append(capo_device_farm.types.insights_type.deserialize_aws_json_1_1(item))
    return out
