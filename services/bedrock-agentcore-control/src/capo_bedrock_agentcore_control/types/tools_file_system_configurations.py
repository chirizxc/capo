"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ToolsFileSystemConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.tools_file_system_configuration

ToolsFileSystemConfigurations: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.tools_file_system_configuration.ToolsFileSystemConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ToolsFileSystemConfigurations) -> list:
    import capo_bedrock_agentcore_control.types.tools_file_system_configuration

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.tools_file_system_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ToolsFileSystemConfigurations:
    import capo_bedrock_agentcore_control.types.tools_file_system_configuration

    out: ToolsFileSystemConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.tools_file_system_configuration.deserialize_json(
                item
            )
        )
    return out
