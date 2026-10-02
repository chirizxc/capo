"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveMetadata``."""

from typing import TypeAlias

AgenticRetrieveMetadata: TypeAlias = dict["str", "object"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AgenticRetrieveMetadata) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> AgenticRetrieveMetadata:
    out: AgenticRetrieveMetadata = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
