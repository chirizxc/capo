"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InsightsFailureSignalList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.insights_failure_signal

InsightsFailureSignalList: TypeAlias = list[
    "capo_bedrock_agentcore.types.insights_failure_signal.InsightsFailureSignal"
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightsFailureSignalList) -> list:
    import capo_bedrock_agentcore.types.insights_failure_signal

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.insights_failure_signal.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> InsightsFailureSignalList:
    import capo_bedrock_agentcore.types.insights_failure_signal

    out: InsightsFailureSignalList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.insights_failure_signal.deserialize_json(item)
        )
    return out
