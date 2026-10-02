"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#LogGroupNamePrefixList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.log_group_name_prefix

LogGroupNamePrefixList: TypeAlias = list[
    "capo_bedrock_agentcore.types.log_group_name_prefix.LogGroupNamePrefix"
]


# --- restJson1 ser/de ---
def serialize_json(value: LogGroupNamePrefixList) -> list:
    return list(value)


def deserialize_json(data: list) -> LogGroupNamePrefixList:
    return [item for item in data if item is not None]
