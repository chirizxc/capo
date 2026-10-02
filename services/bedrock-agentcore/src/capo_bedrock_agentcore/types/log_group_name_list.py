"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#LogGroupNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.log_group_name

LogGroupNameList: TypeAlias = list[
    "capo_bedrock_agentcore.types.log_group_name.LogGroupName"
]


# --- restJson1 ser/de ---
def serialize_json(value: LogGroupNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> LogGroupNameList:
    return [item for item in data if item is not None]
