"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#LimitEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.limit_entry

LimitEntries: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.limit_entry.LimitEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: LimitEntries) -> list:
    import capo_bedrock_agentcore_control.types.limit_entry

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.limit_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> LimitEntries:
    import capo_bedrock_agentcore_control.types.limit_entry

    out: LimitEntries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.limit_entry.deserialize_json(item)
        )
    return out
