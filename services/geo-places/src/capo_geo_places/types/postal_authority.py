"""Generated from Smithy shape ``com.amazonaws.geoplaces#PostalAuthority``."""

from typing import Literal, TypeAlias, cast

PostalAuthority: TypeAlias = Literal["Usps",]


# --- restJson1 ser/de ---
def serialize_json(value: PostalAuthority) -> str:
    return value


def deserialize_json(data: str) -> PostalAuthority:
    return cast(PostalAuthority, data)
