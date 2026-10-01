"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ComputeConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.ec2_configuration


class _ComputeConfiguration_ec2Configuration(TypedDict, closed=True):
    ec2Configuration: (
        "capo_bedrock_agentcore_control.types.ec2_configuration.Ec2Configuration"
    )


ComputeConfiguration: TypeAlias = _ComputeConfiguration_ec2Configuration


# --- restJson1 ser/de ---
def serialize_json(value: ComputeConfiguration) -> dict:
    if "ec2Configuration" in value:
        import capo_bedrock_agentcore_control.types.ec2_configuration

        return {
            "ec2Configuration": capo_bedrock_agentcore_control.types.ec2_configuration.serialize_json(
                value["ec2Configuration"]
            )
        }
    else:
        raise SerializationError("ComputeConfiguration: no variant present")


def deserialize_json(data: dict) -> ComputeConfiguration:
    if data.get("ec2Configuration") is not None:
        import capo_bedrock_agentcore_control.types.ec2_configuration

        return {
            "ec2Configuration": capo_bedrock_agentcore_control.types.ec2_configuration.deserialize_json(
                data["ec2Configuration"]
            )
        }
    else:
        raise DeserializationError("ComputeConfiguration: no recognized variant key")
