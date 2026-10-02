"""Generated from Smithy shape ``com.amazonaws.healthlake#TagMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_healthlake.types.data_transformation_tag_key
    import capo_healthlake.types.data_transformation_tag_value

TagMap: TypeAlias = dict[
    "capo_healthlake.types.data_transformation_tag_key.DataTransformationTagKey",
    "capo_healthlake.types.data_transformation_tag_value.DataTransformationTagValue",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: TagMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> TagMap:
    out: TagMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
