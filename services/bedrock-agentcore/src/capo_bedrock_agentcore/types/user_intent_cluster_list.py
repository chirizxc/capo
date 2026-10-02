"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#UserIntentClusterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.user_intent_cluster

UserIntentClusterList: TypeAlias = list[
    "capo_bedrock_agentcore.types.user_intent_cluster.UserIntentCluster"
]


# --- restJson1 ser/de ---
def serialize_json(value: UserIntentClusterList) -> list:
    import capo_bedrock_agentcore.types.user_intent_cluster

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.user_intent_cluster.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> UserIntentClusterList:
    import capo_bedrock_agentcore.types.user_intent_cluster

    out: UserIntentClusterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.user_intent_cluster.deserialize_json(item)
        )
    return out
