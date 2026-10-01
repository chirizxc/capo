"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AgentRuntimeVersionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_runtime_version_summary

AgentRuntimeVersionSummaryList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.agent_runtime_version_summary.AgentRuntimeVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentRuntimeVersionSummaryList) -> list:
    import capo_bedrock_agentcore_control.types.agent_runtime_version_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.agent_runtime_version_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AgentRuntimeVersionSummaryList:
    import capo_bedrock_agentcore_control.types.agent_runtime_version_summary

    out: AgentRuntimeVersionSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.agent_runtime_version_summary.deserialize_json(
                item
            )
        )
    return out
