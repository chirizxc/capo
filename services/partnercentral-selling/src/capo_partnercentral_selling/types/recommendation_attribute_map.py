"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#RecommendationAttributeMap``."""

from typing import TypeAlias

RecommendationAttributeMap: TypeAlias = dict["str", "str"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: RecommendationAttributeMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> RecommendationAttributeMap:
    out: RecommendationAttributeMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
