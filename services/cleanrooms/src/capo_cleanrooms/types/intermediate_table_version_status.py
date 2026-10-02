"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IntermediateTableVersionStatus``."""

from typing import Literal, TypeAlias, cast

IntermediateTableVersionStatus: TypeAlias = Literal[
    "POPULATE_STARTED",
    "POPULATE_SUCCESS",
    "POPULATE_FAILED",
    "RETENTION_PERIOD_EXPIRED",
]


# --- restJson1 ser/de ---
def serialize_json(value: IntermediateTableVersionStatus) -> str:
    return value


def deserialize_json(data: str) -> IntermediateTableVersionStatus:
    return cast(IntermediateTableVersionStatus, data)
