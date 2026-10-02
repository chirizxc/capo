"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DeleteCapacityProviderSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.capacity_provider_id
    import capo_bedrock_agentcore.types.session_id


class DeleteCapacityProviderSessionRequest(TypedDict, closed=True):
    capacity_provider_id: (
        "capo_bedrock_agentcore.types.capacity_provider_id.CapacityProviderId"
    )
    """<p>The unique identifier of the capacity provider associated with the session.</p>"""
    session_id: "capo_bedrock_agentcore.types.session_id.SessionId"
    """<p>The unique identifier of the capacity provider session to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCapacityProviderSessionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCapacityProviderSessionRequest:
    out: DeleteCapacityProviderSessionRequest = {}  # type: ignore[typeddict-item]
    return out
