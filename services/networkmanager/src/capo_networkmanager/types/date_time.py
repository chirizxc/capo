"""Generated from Smithy shape ``com.amazonaws.networkmanager#DateTime``."""

import datetime
from typing import TypeAlias

DateTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: DateTime) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> DateTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
