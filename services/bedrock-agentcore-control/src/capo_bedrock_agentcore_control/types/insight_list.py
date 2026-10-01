"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#InsightList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.insight

InsightList: TypeAlias = list["capo_bedrock_agentcore_control.types.insight.Insight"]


# --- restJson1 ser/de ---
def serialize_json(value: InsightList) -> list:
    import capo_bedrock_agentcore_control.types.insight

    out: list = []
    for item in value:
        out.append(capo_bedrock_agentcore_control.types.insight.serialize_json(item))
    return out


def deserialize_json(data: list) -> InsightList:
    import capo_bedrock_agentcore_control.types.insight

    out: InsightList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agentcore_control.types.insight.deserialize_json(item))
    return out
