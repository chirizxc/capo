"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#FailureCategoryClusterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.failure_category_cluster

FailureCategoryClusterList: TypeAlias = list[
    "capo_bedrock_agentcore.types.failure_category_cluster.FailureCategoryCluster"
]


# --- restJson1 ser/de ---
def serialize_json(value: FailureCategoryClusterList) -> list:
    import capo_bedrock_agentcore.types.failure_category_cluster

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.failure_category_cluster.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FailureCategoryClusterList:
    import capo_bedrock_agentcore.types.failure_category_cluster

    out: FailureCategoryClusterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.failure_category_cluster.deserialize_json(item)
        )
    return out
