"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#AffectedSessionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.affected_session

AffectedSessionList: TypeAlias = list[
    "capo_bedrock_agentcore.types.affected_session.AffectedSession"
]


# --- restJson1 ser/de ---
def serialize_json(value: AffectedSessionList) -> list:
    import capo_bedrock_agentcore.types.affected_session

    out: list = []
    for item in value:
        out.append(capo_bedrock_agentcore.types.affected_session.serialize_json(item))
    return out


def deserialize_json(data: list) -> AffectedSessionList:
    import capo_bedrock_agentcore.types.affected_session

    out: AffectedSessionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agentcore.types.affected_session.deserialize_json(item))
    return out
