"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EphemeralBlockDeviceMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.ephemeral_block_device_mapping

EphemeralBlockDeviceMappingList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.ephemeral_block_device_mapping.EphemeralBlockDeviceMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: EphemeralBlockDeviceMappingList) -> list:
    import capo_bedrock_agentcore_control.types.ephemeral_block_device_mapping

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.ephemeral_block_device_mapping.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EphemeralBlockDeviceMappingList:
    import capo_bedrock_agentcore_control.types.ephemeral_block_device_mapping

    out: EphemeralBlockDeviceMappingList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.ephemeral_block_device_mapping.deserialize_json(
                item
            )
        )
    return out
