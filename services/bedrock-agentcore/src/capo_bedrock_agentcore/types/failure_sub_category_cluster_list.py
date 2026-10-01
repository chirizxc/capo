"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#FailureSubCategoryClusterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.failure_sub_category_cluster

FailureSubCategoryClusterList: TypeAlias = list[
    "capo_bedrock_agentcore.types.failure_sub_category_cluster.FailureSubCategoryCluster"
]


# --- restJson1 ser/de ---
def serialize_json(value: FailureSubCategoryClusterList) -> list:
    import capo_bedrock_agentcore.types.failure_sub_category_cluster

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.failure_sub_category_cluster.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FailureSubCategoryClusterList:
    import capo_bedrock_agentcore.types.failure_sub_category_cluster

    out: FailureSubCategoryClusterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.failure_sub_category_cluster.deserialize_json(
                item
            )
        )
    return out
