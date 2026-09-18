"""Generated from Smithy shape ``com.amazonaws.deadline#CreatedAt``."""

import datetime
from typing import TypeAlias

CreatedAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: CreatedAt) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def deserialize_json(data: str) -> CreatedAt:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))
