"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ExecutionSummaryClusterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.execution_summary_cluster

ExecutionSummaryClusterList: TypeAlias = list[
    "capo_bedrock_agentcore.types.execution_summary_cluster.ExecutionSummaryCluster"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionSummaryClusterList) -> list:
    import capo_bedrock_agentcore.types.execution_summary_cluster

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.execution_summary_cluster.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ExecutionSummaryClusterList:
    import capo_bedrock_agentcore.types.execution_summary_cluster

    out: ExecutionSummaryClusterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.execution_summary_cluster.deserialize_json(
                item
            )
        )
    return out
