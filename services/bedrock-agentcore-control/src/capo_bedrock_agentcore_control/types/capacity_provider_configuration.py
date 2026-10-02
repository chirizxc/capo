"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CapacityProviderConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.capacity_provider_arn


class CapacityProviderConfiguration(TypedDict, closed=True):
    capacity_provider_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.capacity_provider_arn.CapacityProviderArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the capacity provider to use for the AgentCore Runtime.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapacityProviderConfiguration) -> dict:
    out: dict = {}
    if "capacity_provider_arn" in value:
        out["capacityProviderArn"] = value["capacity_provider_arn"]
    return out


def deserialize_json(data: dict) -> CapacityProviderConfiguration:
    out: CapacityProviderConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("capacityProviderArn") is not None:
        out["capacity_provider_arn"] = data["capacityProviderArn"]
    return out
