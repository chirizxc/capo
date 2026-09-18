"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#LastUpdatedAt``."""

import datetime
from typing import TypeAlias

LastUpdatedAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: LastUpdatedAt) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> LastUpdatedAt:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
