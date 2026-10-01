"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PrivateKeySource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.kms_key_source_type


class _PrivateKeySource_kmsKeySource(TypedDict, closed=True):
    kmsKeySource: (
        "capo_bedrock_agentcore_control.types.kms_key_source_type.KmsKeySourceType"
    )


PrivateKeySource: TypeAlias = _PrivateKeySource_kmsKeySource


# --- restJson1 ser/de ---
def serialize_json(value: PrivateKeySource) -> dict:
    if "kmsKeySource" in value:
        import capo_bedrock_agentcore_control.types.kms_key_source_type

        return {
            "kmsKeySource": capo_bedrock_agentcore_control.types.kms_key_source_type.serialize_json(
                value["kmsKeySource"]
            )
        }
    else:
        raise SerializationError("PrivateKeySource: no variant present")


def deserialize_json(data: dict) -> PrivateKeySource:
    if data.get("kmsKeySource") is not None:
        import capo_bedrock_agentcore_control.types.kms_key_source_type

        return {
            "kmsKeySource": capo_bedrock_agentcore_control.types.kms_key_source_type.deserialize_json(
                data["kmsKeySource"]
            )
        }
    else:
        raise DeserializationError("PrivateKeySource: no recognized variant key")
