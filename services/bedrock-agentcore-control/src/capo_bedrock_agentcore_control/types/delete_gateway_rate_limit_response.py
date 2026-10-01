"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteGatewayRateLimitResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_id
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_status


class DeleteGatewayRateLimitResponse(TypedDict, closed=True):
    rate_limit_id: (
        "capo_bedrock_agentcore_control.types.gateway_rate_limit_id.GatewayRateLimitId"
    )
    """<p>The unique identifier of the deleted rate limit.</p>"""
    status: "capo_bedrock_agentcore_control.types.gateway_rate_limit_status.GatewayRateLimitStatus"
    """<p>The current status of the rate limit deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGatewayRateLimitResponse) -> dict:
    out: dict = {}
    out["rateLimitId"] = value["rate_limit_id"]
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.gateway_rate_limit_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteGatewayRateLimitResponse:
    out: DeleteGatewayRateLimitResponse = {}  # type: ignore[typeddict-item]
    if data.get("rateLimitId") is not None:
        out["rate_limit_id"] = data["rateLimitId"]
    else:
        raise DeserializationError(
            "DeleteGatewayRateLimitResponse.rate_limit_id required"
        )
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.gateway_rate_limit_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.gateway_rate_limit_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DeleteGatewayRateLimitResponse.status required")
    return out
