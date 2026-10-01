"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#DocumentOutputFormat``."""

from typing import Literal, TypeAlias, cast

DocumentOutputFormat: TypeAlias = Literal[
    "RAW",
    "EXTRACTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentOutputFormat) -> str:
    return value


def deserialize_json(data: str) -> DocumentOutputFormat:
    return cast(DocumentOutputFormat, data)
