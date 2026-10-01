"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListGatewayRateLimitsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.gateway_identifier
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_max_results
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_next_token


class ListGatewayRateLimitsRequest(TypedDict, closed=True):
    gateway_identifier: (
        "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier"
    )
    """<p>The unique identifier of the gateway.</p>"""
    max_results: NotRequired[
        "capo_bedrock_agentcore_control.types.gateway_rate_limit_max_results.GatewayRateLimitMaxResults"
    ]
    """<p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>"""
    next_token: NotRequired[
        "capo_bedrock_agentcore_control.types.gateway_rate_limit_next_token.GatewayRateLimitNextToken"
    ]
    """<p>The token to use to retrieve the next page of results. Use the value returned in a previous <code>ListGatewayRateLimits</code> response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGatewayRateLimitsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListGatewayRateLimitsRequest:
    out: ListGatewayRateLimitsRequest = {}  # type: ignore[typeddict-item]
    return out
