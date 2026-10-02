"""Generated from Smithy shape ``com.amazonaws.dynamodb#VectorDistanceFunction``."""

from typing import Literal, TypeAlias, cast

VectorDistanceFunction: TypeAlias = Literal[
    "COSINE",
    "DOT_PRODUCT",
    "EUCLIDEAN",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VectorDistanceFunction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> VectorDistanceFunction:
    return cast(VectorDistanceFunction, data)
