"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ClusteringFrequencyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.clustering_frequency

ClusteringFrequencyList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.clustering_frequency.ClusteringFrequency"
]


# --- restJson1 ser/de ---
def serialize_json(value: ClusteringFrequencyList) -> list:
    import capo_bedrock_agentcore_control.types.clustering_frequency

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.clustering_frequency.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ClusteringFrequencyList:
    import capo_bedrock_agentcore_control.types.clustering_frequency

    out: ClusteringFrequencyList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.clustering_frequency.deserialize_json(
                item
            )
        )
    return out
