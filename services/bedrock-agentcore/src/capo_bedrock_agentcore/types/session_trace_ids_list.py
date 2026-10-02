"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SessionTraceIdsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.session_trace_ids

SessionTraceIdsList: TypeAlias = list[
    "capo_bedrock_agentcore.types.session_trace_ids.SessionTraceIds"
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionTraceIdsList) -> list:
    import capo_bedrock_agentcore.types.session_trace_ids

    out: list = []
    for item in value:
        out.append(capo_bedrock_agentcore.types.session_trace_ids.serialize_json(item))
    return out


def deserialize_json(data: list) -> SessionTraceIdsList:
    import capo_bedrock_agentcore.types.session_trace_ids

    out: SessionTraceIdsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.session_trace_ids.deserialize_json(item)
        )
    return out
