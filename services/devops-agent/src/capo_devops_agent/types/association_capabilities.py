"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssociationCapabilities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_agent.types.capability_configuration
    import capo_devops_agent.types.capability_type

AssociationCapabilities: TypeAlias = dict[
    "capo_devops_agent.types.capability_type.CapabilityType",
    "capo_devops_agent.types.capability_configuration.CapabilityConfiguration",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AssociationCapabilities) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_devops_agent.types.capability_configuration
        import capo_devops_agent.types.capability_type

        out[capo_devops_agent.types.capability_type.serialize_json(key)] = (
            capo_devops_agent.types.capability_configuration.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> AssociationCapabilities:
    out: AssociationCapabilities = {}
    for key, value in data.items():
        import capo_devops_agent.types.capability_type

        if value is None:
            continue
        import capo_devops_agent.types.capability_configuration

        out[capo_devops_agent.types.capability_type.deserialize_json(key)] = (
            capo_devops_agent.types.capability_configuration.deserialize_json(value)
        )
    return out
