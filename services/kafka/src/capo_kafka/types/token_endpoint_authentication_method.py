"""Generated from Smithy shape ``com.amazonaws.kafka#TokenEndpointAuthenticationMethod``."""

from typing import Literal, TypeAlias, cast

"""<p>How client credentials are sent to the identity provider's token endpoint.</p>"""
TokenEndpointAuthenticationMethod: TypeAlias = Literal[
    "POST",
    "BASIC",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: TokenEndpointAuthenticationMethod) -> str:
    return value


def deserialize_json(data: str) -> TokenEndpointAuthenticationMethod:
    return cast(TokenEndpointAuthenticationMethod, data)
