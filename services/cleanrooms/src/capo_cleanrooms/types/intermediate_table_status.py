"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IntermediateTableStatus``."""

from typing import Literal, TypeAlias, cast

IntermediateTableStatus: TypeAlias = Literal[
    "CREATED",
    "POPULATE_STARTED",
    "POPULATE_SUCCESS",
    "POPULATE_FAILED",
    "DISALLOWED_BY_DATA_PROVIDER",
    "BASE_TABLE_REMOVED",
    "RETENTION_PERIOD_EXPIRED",
]


# --- restJson1 ser/de ---
def serialize_json(value: IntermediateTableStatus) -> str:
    return value


def deserialize_json(data: str) -> IntermediateTableStatus:
    return cast(IntermediateTableStatus, data)
