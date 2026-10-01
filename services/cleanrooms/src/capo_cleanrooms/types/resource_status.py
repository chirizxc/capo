"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ResourceStatus``."""

from typing import Literal, TypeAlias, cast

ResourceStatus: TypeAlias = Literal[
    "CREATED",
    "POPULATE_STARTED",
    "POPULATE_SUCCESS",
    "POPULATE_FAILED",
    "DISALLOWED_BY_DATA_PROVIDER",
    "BASE_TABLE_REMOVED",
    "RETENTION_PERIOD_EXPIRED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceStatus) -> str:
    return value


def deserialize_json(data: str) -> ResourceStatus:
    return cast(ResourceStatus, data)
