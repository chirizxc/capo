"""Generated from Smithy shape ``com.amazonaws.glue#TableResourceShareType``."""

from typing import Literal, TypeAlias, cast

TableResourceShareType: TypeAlias = Literal[
    "FEDERATED",
    "ALL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableResourceShareType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TableResourceShareType:
    return cast(TableResourceShareType, data)
