"""Generated from Smithy shape ``com.amazonaws.opensearch#LastUpdated``."""

import datetime
from typing import TypeAlias

LastUpdated: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: LastUpdated) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> LastUpdated:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
