"""Generated from Smithy shape ``com.amazonaws.appconfig#DeleteType``."""

from typing import Literal, TypeAlias, cast

DeleteType: TypeAlias = Literal[
    "ARCHIVE",
    "DESTROY",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteType) -> str:
    return value


def deserialize_json(data: str) -> DeleteType:
    return cast(DeleteType, data)
