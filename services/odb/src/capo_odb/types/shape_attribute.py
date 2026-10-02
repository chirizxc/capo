"""Generated from Smithy shape ``com.amazonaws.odb#ShapeAttribute``."""

from typing import Literal, TypeAlias, cast

ShapeAttribute: TypeAlias = Literal[
    "SMART_STORAGE",
    "BLOCK_STORAGE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ShapeAttribute) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ShapeAttribute:
    return cast(ShapeAttribute, data)
