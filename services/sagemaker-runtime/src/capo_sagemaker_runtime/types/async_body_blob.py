"""Generated from Smithy shape ``com.amazonaws.sagemakerruntime#AsyncBodyBlob``."""

import base64
from typing import TypeAlias

AsyncBodyBlob: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: AsyncBodyBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> AsyncBodyBlob:
    return base64.b64decode(data)
