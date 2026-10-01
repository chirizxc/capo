"""Generated from Smithy shape ``com.amazonaws.geoplaces#PostalCodeType``."""

from typing import Literal, TypeAlias, cast

PostalCodeType: TypeAlias = Literal[
    "UspsZip",
    "UspsZipPlus4",
]


# --- restJson1 ser/de ---
def serialize_json(value: PostalCodeType) -> str:
    return value


def deserialize_json(data: str) -> PostalCodeType:
    return cast(PostalCodeType, data)
