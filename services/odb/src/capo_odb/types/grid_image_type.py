"""Generated from Smithy shape ``com.amazonaws.odb#GridImageType``."""

from typing import Literal, TypeAlias, cast

GridImageType: TypeAlias = Literal[
    "RELEASE_UPDATE",
    "CUSTOM_IMAGE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GridImageType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> GridImageType:
    return cast(GridImageType, data)
