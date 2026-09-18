"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DestinationUpdatedAt``."""

import datetime
from typing import TypeAlias

DestinationUpdatedAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: DestinationUpdatedAt) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> DestinationUpdatedAt:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
