"""Generated from Smithy shape ``com.amazonaws.notifications#LastActivationTime``."""

import datetime
from typing import TypeAlias

LastActivationTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: LastActivationTime) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def deserialize_json(data: str) -> LastActivationTime:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))
