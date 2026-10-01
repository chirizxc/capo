"""Generated from Smithy shape ``com.amazonaws.geoplaces#PostalCodeMode``."""

from typing import Literal, TypeAlias, cast

PostalCodeMode: TypeAlias = Literal[
    "MergeAllSpannedLocalities",
    "EnumerateSpannedLocalities",
    "EnumerateSpannedDistricts",
]


# --- restJson1 ser/de ---
def serialize_json(value: PostalCodeMode) -> str:
    return value


def deserialize_json(data: str) -> PostalCodeMode:
    return cast(PostalCodeMode, data)
