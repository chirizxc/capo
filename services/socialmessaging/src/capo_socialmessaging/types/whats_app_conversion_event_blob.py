"""Generated from Smithy shape ``com.amazonaws.socialmessaging#WhatsAppConversionEventBlob``."""

import base64
from typing import TypeAlias

WhatsAppConversionEventBlob: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppConversionEventBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> WhatsAppConversionEventBlob:
    return base64.b64decode(data)
