"""Generated from Smithy shape ``com.amazonaws.appconfig#Iso8601DateTime``."""

import datetime
from typing import TypeAlias

Iso8601DateTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: Iso8601DateTime) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def deserialize_json(data: str) -> Iso8601DateTime:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))
