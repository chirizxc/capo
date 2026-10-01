"""Generated from Smithy shape ``com.amazonaws.glue#SubObjectSourceType``."""

from typing import Literal, TypeAlias, cast

SubObjectSourceType: TypeAlias = Literal[
    "HIVE_PARQUET",
    "HIVE_ORC",
    "HIVE_CSV",
    "HIVE_JSON",
    "PLAIN_PARQUET",
    "ICEBERG",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubObjectSourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SubObjectSourceType:
    return cast(SubObjectSourceType, data)
