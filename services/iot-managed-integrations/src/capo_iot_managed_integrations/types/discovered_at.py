"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DiscoveredAt``."""

import datetime
from typing import TypeAlias

DiscoveredAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: DiscoveredAt) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> DiscoveredAt:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
