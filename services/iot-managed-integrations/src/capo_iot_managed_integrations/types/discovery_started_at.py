"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DiscoveryStartedAt``."""

import datetime
from typing import TypeAlias

DiscoveryStartedAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: DiscoveryStartedAt) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> DiscoveryStartedAt:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
