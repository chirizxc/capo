"""Generated from Smithy shape ``com.amazonaws.synthetics#ReplicationState``."""

from typing import Literal, TypeAlias, cast

ReplicationState: TypeAlias = Literal[
    "InProgress",
    "InSync",
    "Inconsistent",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationState) -> str:
    return value


def deserialize_json(data: str) -> ReplicationState:
    return cast(ReplicationState, data)
