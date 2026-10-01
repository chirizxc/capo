"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#StreamUrlStatus``."""

from typing import Literal, TypeAlias, cast

StreamUrlStatus: TypeAlias = Literal[
    "ACTIVE",
    "EXPIRED",
    "REVOKED",
    "LIMIT_REACHED",
]


# --- restJson1 ser/de ---
def serialize_json(value: StreamUrlStatus) -> str:
    return value


def deserialize_json(data: str) -> StreamUrlStatus:
    return cast(StreamUrlStatus, data)
