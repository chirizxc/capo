"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewayRateLimits``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_detail

GatewayRateLimits: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.gateway_rate_limit_detail.GatewayRateLimitDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: GatewayRateLimits) -> list:
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_detail

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.gateway_rate_limit_detail.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GatewayRateLimits:
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_detail

    out: GatewayRateLimits = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.gateway_rate_limit_detail.deserialize_json(
                item
            )
        )
    return out
