"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveTraceResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_trace_result_item

AgenticRetrieveTraceResults: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.agentic_retrieve_trace_result_item.AgenticRetrieveTraceResultItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveTraceResults) -> list:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_trace_result_item

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.agentic_retrieve_trace_result_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AgenticRetrieveTraceResults:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_trace_result_item

    out: AgenticRetrieveTraceResults = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.agentic_retrieve_trace_result_item.deserialize_json(
                item
            )
        )
    return out
