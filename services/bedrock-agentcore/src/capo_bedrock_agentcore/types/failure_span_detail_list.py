"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#FailureSpanDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.failure_span_detail

FailureSpanDetailList: TypeAlias = list[
    "capo_bedrock_agentcore.types.failure_span_detail.FailureSpanDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: FailureSpanDetailList) -> list:
    import capo_bedrock_agentcore.types.failure_span_detail

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.failure_span_detail.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FailureSpanDetailList:
    import capo_bedrock_agentcore.types.failure_span_detail

    out: FailureSpanDetailList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.failure_span_detail.deserialize_json(item)
        )
    return out
