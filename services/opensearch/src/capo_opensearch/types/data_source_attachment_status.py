"""Generated from Smithy shape ``com.amazonaws.opensearch#DataSourceAttachmentStatus``."""

from typing import Literal, TypeAlias, cast

DataSourceAttachmentStatus: TypeAlias = Literal[
    "PENDING",
    "ATTACHED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceAttachmentStatus) -> str:
    return value


def deserialize_json(data: str) -> DataSourceAttachmentStatus:
    return cast(DataSourceAttachmentStatus, data)
