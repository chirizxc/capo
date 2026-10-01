"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CapacityProviderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.capacity_provider_summary

CapacityProviderList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.capacity_provider_summary.CapacityProviderSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CapacityProviderList) -> list:
    import capo_bedrock_agentcore_control.types.capacity_provider_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.capacity_provider_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CapacityProviderList:
    import capo_bedrock_agentcore_control.types.capacity_provider_summary

    out: CapacityProviderList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.capacity_provider_summary.deserialize_json(
                item
            )
        )
    return out
