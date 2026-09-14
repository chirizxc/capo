"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DestinationCreatedAt``."""

import datetime
from typing import TypeAlias

DestinationCreatedAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: DestinationCreatedAt) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> DestinationCreatedAt:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
