"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResaleAuthorizationResellerRoleString``."""

from typing import Literal, TypeAlias, cast

ResaleAuthorizationResellerRoleString: TypeAlias = Literal[
    "ChannelPartner",
    "Distributor",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResaleAuthorizationResellerRoleString) -> str:
    return value


def deserialize_json(data: str) -> ResaleAuthorizationResellerRoleString:
    return cast(ResaleAuthorizationResellerRoleString, data)
