"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HostingEnvironmentListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.hosting_environment

HostingEnvironmentListType: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.hosting_environment.HostingEnvironment"
]


# --- restJson1 ser/de ---
def serialize_json(value: HostingEnvironmentListType) -> list:
    import capo_bedrock_agentcore_control.types.hosting_environment

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.hosting_environment.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> HostingEnvironmentListType:
    import capo_bedrock_agentcore_control.types.hosting_environment

    out: HostingEnvironmentListType = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.hosting_environment.deserialize_json(
                item
            )
        )
    return out
