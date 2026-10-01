"""Generated from Smithy shape ``com.amazonaws.geoplaces#AdminNamesPreference``."""

from typing import Literal, TypeAlias, cast

AdminNamesPreference: TypeAlias = Literal[
    "Alternative",
    "Primary",
]


# --- restJson1 ser/de ---
def serialize_json(value: AdminNamesPreference) -> str:
    return value


def deserialize_json(data: str) -> AdminNamesPreference:
    return cast(AdminNamesPreference, data)
