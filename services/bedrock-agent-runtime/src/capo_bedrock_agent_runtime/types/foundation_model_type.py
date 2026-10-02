"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FoundationModelType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of foundation model.</p>"""
FoundationModelType: TypeAlias = Literal[
    "CUSTOM",
    "MANAGED",
]


# --- restJson1 ser/de ---
def serialize_json(value: FoundationModelType) -> str:
    return value


def deserialize_json(data: str) -> FoundationModelType:
    return cast(FoundationModelType, data)
