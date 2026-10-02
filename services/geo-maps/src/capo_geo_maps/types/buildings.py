"""Generated from Smithy shape ``com.amazonaws.geomaps#Buildings``."""

from typing import Literal, TypeAlias, cast

Buildings: TypeAlias = Literal["Buildings3D",]


# --- restJson1 ser/de ---
def serialize_json(value: Buildings) -> str:
    return value


def deserialize_json(data: str) -> Buildings:
    return cast(Buildings, data)
