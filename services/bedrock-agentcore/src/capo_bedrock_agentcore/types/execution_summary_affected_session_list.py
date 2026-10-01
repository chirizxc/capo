"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ExecutionSummaryAffectedSessionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.execution_summary_affected_session

ExecutionSummaryAffectedSessionList: TypeAlias = list[
    "capo_bedrock_agentcore.types.execution_summary_affected_session.ExecutionSummaryAffectedSession"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionSummaryAffectedSessionList) -> list:
    import capo_bedrock_agentcore.types.execution_summary_affected_session

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.execution_summary_affected_session.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ExecutionSummaryAffectedSessionList:
    import capo_bedrock_agentcore.types.execution_summary_affected_session

    out: ExecutionSummaryAffectedSessionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.execution_summary_affected_session.deserialize_json(
                item
            )
        )
    return out
