"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ChildResourceType``."""

from typing import Literal, TypeAlias, cast

ChildResourceType: TypeAlias = Literal["INTERMEDIATE_TABLE",]


# --- restJson1 ser/de ---
def serialize_json(value: ChildResourceType) -> str:
    return value


def deserialize_json(data: str) -> ChildResourceType:
    return cast(ChildResourceType, data)
