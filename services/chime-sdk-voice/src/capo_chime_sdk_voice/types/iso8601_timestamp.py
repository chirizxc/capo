"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#Iso8601Timestamp``."""

import datetime
from typing import TypeAlias

Iso8601Timestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: Iso8601Timestamp) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def deserialize_json(data: str) -> Iso8601Timestamp:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))
