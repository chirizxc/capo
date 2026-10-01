"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#UserIntentAffectedSessionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.user_intent_affected_session

UserIntentAffectedSessionList: TypeAlias = list[
    "capo_bedrock_agentcore.types.user_intent_affected_session.UserIntentAffectedSession"
]


# --- restJson1 ser/de ---
def serialize_json(value: UserIntentAffectedSessionList) -> list:
    import capo_bedrock_agentcore.types.user_intent_affected_session

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.user_intent_affected_session.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> UserIntentAffectedSessionList:
    import capo_bedrock_agentcore.types.user_intent_affected_session

    out: UserIntentAffectedSessionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.user_intent_affected_session.deserialize_json(
                item
            )
        )
    return out
