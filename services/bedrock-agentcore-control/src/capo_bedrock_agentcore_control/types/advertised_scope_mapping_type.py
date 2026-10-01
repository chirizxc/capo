"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AdvertisedScopeMappingType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.allowed_scope_type

AdvertisedScopeMappingType: TypeAlias = dict[
    "capo_bedrock_agentcore_control.types.allowed_scope_type.AllowedScopeType",
    "capo_bedrock_agentcore_control.types.allowed_scope_type.AllowedScopeType",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AdvertisedScopeMappingType) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> AdvertisedScopeMappingType:
    out: AdvertisedScopeMappingType = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
