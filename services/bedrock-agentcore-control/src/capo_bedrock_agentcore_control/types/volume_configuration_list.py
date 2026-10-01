"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#VolumeConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.volume_configuration

VolumeConfigurationList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.volume_configuration.VolumeConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: VolumeConfigurationList) -> list:
    import capo_bedrock_agentcore_control.types.volume_configuration

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.volume_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> VolumeConfigurationList:
    import capo_bedrock_agentcore_control.types.volume_configuration

    out: VolumeConfigurationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.volume_configuration.deserialize_json(
                item
            )
        )
    return out
