"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessMemoryConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_agent_core_memory_configuration
    import capo_bedrock_agentcore_control.types.harness_disabled_memory_configuration
    import capo_bedrock_agentcore_control.types.harness_managed_memory_configuration


class _HarnessMemoryConfiguration_agentCoreMemoryConfiguration(TypedDict, closed=True):
    agentCoreMemoryConfiguration: "capo_bedrock_agentcore_control.types.harness_agent_core_memory_configuration.HarnessAgentCoreMemoryConfiguration"


class _HarnessMemoryConfiguration_managedMemoryConfiguration(TypedDict, closed=True):
    managedMemoryConfiguration: "capo_bedrock_agentcore_control.types.harness_managed_memory_configuration.HarnessManagedMemoryConfiguration"


class _HarnessMemoryConfiguration_disabled(TypedDict, closed=True):
    disabled: "capo_bedrock_agentcore_control.types.harness_disabled_memory_configuration.HarnessDisabledMemoryConfiguration"


HarnessMemoryConfiguration: TypeAlias = (
    _HarnessMemoryConfiguration_agentCoreMemoryConfiguration
    | _HarnessMemoryConfiguration_managedMemoryConfiguration
    | _HarnessMemoryConfiguration_disabled
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessMemoryConfiguration) -> dict:
    if "agentCoreMemoryConfiguration" in value:
        import capo_bedrock_agentcore_control.types.harness_agent_core_memory_configuration

        return {
            "agentCoreMemoryConfiguration": capo_bedrock_agentcore_control.types.harness_agent_core_memory_configuration.serialize_json(
                value["agentCoreMemoryConfiguration"]
            )
        }
    elif "managedMemoryConfiguration" in value:
        import capo_bedrock_agentcore_control.types.harness_managed_memory_configuration

        return {
            "managedMemoryConfiguration": capo_bedrock_agentcore_control.types.harness_managed_memory_configuration.serialize_json(
                value["managedMemoryConfiguration"]
            )
        }
    elif "disabled" in value:
        import capo_bedrock_agentcore_control.types.harness_disabled_memory_configuration

        return {
            "disabled": capo_bedrock_agentcore_control.types.harness_disabled_memory_configuration.serialize_json(
                value["disabled"]
            )
        }
    else:
        raise SerializationError("HarnessMemoryConfiguration: no variant present")


def deserialize_json(data: dict) -> HarnessMemoryConfiguration:
    if data.get("agentCoreMemoryConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.harness_agent_core_memory_configuration

        return {
            "agentCoreMemoryConfiguration": capo_bedrock_agentcore_control.types.harness_agent_core_memory_configuration.deserialize_json(
                data["agentCoreMemoryConfiguration"]
            )
        }
    elif data.get("managedMemoryConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.harness_managed_memory_configuration

        return {
            "managedMemoryConfiguration": capo_bedrock_agentcore_control.types.harness_managed_memory_configuration.deserialize_json(
                data["managedMemoryConfiguration"]
            )
        }
    elif data.get("disabled") is not None:
        import capo_bedrock_agentcore_control.types.harness_disabled_memory_configuration

        return {
            "disabled": capo_bedrock_agentcore_control.types.harness_disabled_memory_configuration.deserialize_json(
                data["disabled"]
            )
        }
    else:
        raise DeserializationError(
            "HarnessMemoryConfiguration: no recognized variant key"
        )
