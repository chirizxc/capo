"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetGatewayRateLimitRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.gateway_identifier
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_id


class GetGatewayRateLimitRequest(TypedDict, closed=True):
    gateway_identifier: (
        "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier"
    )
    """<p>The unique identifier of the gateway.</p>"""
    rate_limit_id: (
        "capo_bedrock_agentcore_control.types.gateway_rate_limit_id.GatewayRateLimitId"
    )
    """<p>The unique identifier of the rate limit to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGatewayRateLimitRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetGatewayRateLimitRequest:
    out: GetGatewayRateLimitRequest = {}  # type: ignore[typeddict-item]
    return out
