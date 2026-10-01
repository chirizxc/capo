"""Generated from Smithy shape ``com.amazonaws.socialmessaging#WhatsAppCallEventBlob``."""

import base64
from typing import TypeAlias

WhatsAppCallEventBlob: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppCallEventBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> WhatsAppCallEventBlob:
    return base64.b64decode(data)
