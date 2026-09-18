"""Generated from Smithy shape ``com.amazonaws.iotwireless#LastUpdateTime``."""

import datetime
from typing import TypeAlias

LastUpdateTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: LastUpdateTime) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def deserialize_json(data: str) -> LastUpdateTime:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))
