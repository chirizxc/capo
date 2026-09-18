"""Generated from Smithy shape ``com.amazonaws.panorama#LastUpdatedTime``."""

import datetime
from typing import TypeAlias

LastUpdatedTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: LastUpdatedTime) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> LastUpdatedTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
