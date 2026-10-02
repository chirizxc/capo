"""Generated from Smithy shape ``com.amazonaws.connect#AuthCodeEntityType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of entity associated with an authorization code in Connect Customer.</p>"""
AuthCodeEntityType: TypeAlias = Literal["CUSTOMER_PROFILE",]


# --- restJson1 ser/de ---
def serialize_json(value: AuthCodeEntityType) -> str:
    return value


def deserialize_json(data: str) -> AuthCodeEntityType:
    return cast(AuthCodeEntityType, data)
