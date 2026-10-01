"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#TraceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.trace_id

TraceIdList: TypeAlias = list["capo_bedrock_agentcore.types.trace_id.TraceId"]


# --- restJson1 ser/de ---
def serialize_json(value: TraceIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> TraceIdList:
    return [item for item in data if item is not None]
