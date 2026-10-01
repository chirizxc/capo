"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ConsentPortalSourceType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of a consent portal source. Currently, we only support type <code>agentcore-gateway</code>.</p>"""
ConsentPortalSourceType: TypeAlias = Literal["agentcore-gateway",]


# --- restJson1 ser/de ---
def serialize_json(value: ConsentPortalSourceType) -> str:
    return value


def deserialize_json(data: str) -> ConsentPortalSourceType:
    return cast(ConsentPortalSourceType, data)
