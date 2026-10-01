"""Generated from Smithy shape ``com.amazonaws.cleanrooms#BaseTableDependencyType``."""

from typing import Literal, TypeAlias, cast

BaseTableDependencyType: TypeAlias = Literal[
    "TABLE",
    "INTERMEDIATE_TABLE",
    "ID_MAPPING_TABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: BaseTableDependencyType) -> str:
    return value


def deserialize_json(data: str) -> BaseTableDependencyType:
    return cast(BaseTableDependencyType, data)
