"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#StreamUrlStatusReason``."""

from typing import Literal, TypeAlias, cast

StreamUrlStatusReason: TypeAlias = Literal[
    "userRevoked",
    "revokedAndTerminatingSessions",
    "revokedAndSessionsTerminated",
    "streamGroupDeleted",
    "applicationDeleted",
]


# --- restJson1 ser/de ---
def serialize_json(value: StreamUrlStatusReason) -> str:
    return value


def deserialize_json(data: str) -> StreamUrlStatusReason:
    return cast(StreamUrlStatusReason, data)
