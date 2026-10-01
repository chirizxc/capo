"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveWarnings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_warning

AgenticRetrieveWarnings: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.agentic_retrieve_warning.AgenticRetrieveWarning"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveWarnings) -> list:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_warning

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.agentic_retrieve_warning.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AgenticRetrieveWarnings:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_warning

    out: AgenticRetrieveWarnings = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.agentic_retrieve_warning.deserialize_json(
                item
            )
        )
    return out
