"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_result_item

AgenticRetrieveResults: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.agentic_retrieve_result_item.AgenticRetrieveResultItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveResults) -> list:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_result_item

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.agentic_retrieve_result_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AgenticRetrieveResults:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_result_item

    out: AgenticRetrieveResults = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.agentic_retrieve_result_item.deserialize_json(
                item
            )
        )
    return out
