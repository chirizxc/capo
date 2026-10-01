"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DatasetTypeEnum``."""

from typing import Literal, TypeAlias, cast

DatasetTypeEnum: TypeAlias = Literal[
    "SESSION",
    "CURATED",
    "EXTERNAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetTypeEnum) -> str:
    return value


def deserialize_json(data: str) -> DatasetTypeEnum:
    return cast(DatasetTypeEnum, data)
