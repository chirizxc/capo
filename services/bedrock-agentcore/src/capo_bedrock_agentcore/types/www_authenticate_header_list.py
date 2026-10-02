"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#WwwAuthenticateHeaderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.www_authenticate_header

WwwAuthenticateHeaderList: TypeAlias = list[
    "capo_bedrock_agentcore.types.www_authenticate_header.WwwAuthenticateHeader"
]


# --- restJson1 ser/de ---
def serialize_json(value: WwwAuthenticateHeaderList) -> list:
    return list(value)


def deserialize_json(data: list) -> WwwAuthenticateHeaderList:
    return [item for item in data if item is not None]
