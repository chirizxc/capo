"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#InstanceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.ec2_instance_type

InstanceTypeList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.ec2_instance_type.EC2InstanceType"
]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> InstanceTypeList:
    return [item for item in data if item is not None]
