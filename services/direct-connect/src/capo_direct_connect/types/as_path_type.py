"""Generated from Smithy shape ``com.amazonaws.directconnect#AsPathType``."""

from typing import Literal, TypeAlias, cast

AsPathType: TypeAlias = Literal[
    "seq",
    "set",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AsPathType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AsPathType:
    return cast(AsPathType, data)
