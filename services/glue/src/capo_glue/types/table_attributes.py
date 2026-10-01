"""Generated from Smithy shape ``com.amazonaws.glue#TableAttributes``."""

from typing import Literal, TypeAlias, cast

TableAttributes: TypeAlias = Literal[
    "NAME",
    "TABLE_TYPE",
    "DEFAULT",
    "LATEST_ICEBERG_METADATA",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableAttributes) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TableAttributes:
    return cast(TableAttributes, data)
