"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetCapacityProviderInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.capacity_provider_id


class GetCapacityProviderInput(TypedDict, closed=True):
    capacity_provider_id: (
        "capo_bedrock_agentcore_control.types.capacity_provider_id.CapacityProviderId"
    )
    """<p>The unique identifier of the capacity provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCapacityProviderInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCapacityProviderInput:
    out: GetCapacityProviderInput = {}  # type: ignore[typeddict-item]
    return out
