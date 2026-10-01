"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveFailures``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_failure

AgenticRetrieveFailures: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.agentic_retrieve_failure.AgenticRetrieveFailure"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveFailures) -> list:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_failure

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.agentic_retrieve_failure.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AgenticRetrieveFailures:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_failure

    out: AgenticRetrieveFailures = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.agentic_retrieve_failure.deserialize_json(
                item
            )
        )
    return out
