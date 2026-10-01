"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RootCauseClusterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.root_cause_cluster

RootCauseClusterList: TypeAlias = list[
    "capo_bedrock_agentcore.types.root_cause_cluster.RootCauseCluster"
]


# --- restJson1 ser/de ---
def serialize_json(value: RootCauseClusterList) -> list:
    import capo_bedrock_agentcore.types.root_cause_cluster

    out: list = []
    for item in value:
        out.append(capo_bedrock_agentcore.types.root_cause_cluster.serialize_json(item))
    return out


def deserialize_json(data: list) -> RootCauseClusterList:
    import capo_bedrock_agentcore.types.root_cause_cluster

    out: RootCauseClusterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.root_cause_cluster.deserialize_json(item)
        )
    return out
