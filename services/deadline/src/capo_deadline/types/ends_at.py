"""Generated from Smithy shape ``com.amazonaws.deadline#EndsAt``."""

import datetime
from typing import TypeAlias

EndsAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: EndsAt) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def deserialize_json(data: str) -> EndsAt:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))
