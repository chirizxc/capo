"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#StartedAt``."""

import datetime
from typing import TypeAlias

StartedAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: StartedAt) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> StartedAt:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
