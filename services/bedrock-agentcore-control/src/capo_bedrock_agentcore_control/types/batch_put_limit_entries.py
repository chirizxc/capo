"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#BatchPutLimitEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.batch_put_limit_entry

BatchPutLimitEntries: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.batch_put_limit_entry.BatchPutLimitEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutLimitEntries) -> list:
    import capo_bedrock_agentcore_control.types.batch_put_limit_entry

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.batch_put_limit_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchPutLimitEntries:
    import capo_bedrock_agentcore_control.types.batch_put_limit_entry

    out: BatchPutLimitEntries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.batch_put_limit_entry.deserialize_json(
                item
            )
        )
    return out
