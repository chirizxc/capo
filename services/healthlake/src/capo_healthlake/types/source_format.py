"""Generated from Smithy shape ``com.amazonaws.healthlake#SourceFormat``."""

from typing import Literal, TypeAlias, cast

SourceFormat: TypeAlias = Literal[
    "CCDA",
    "CSV",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SourceFormat) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SourceFormat:
    return cast(SourceFormat, data)
