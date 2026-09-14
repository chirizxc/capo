"""Generated from Smithy shape ``com.amazonaws.iot#LastUpdatedAtDate``."""

import datetime
from typing import TypeAlias

LastUpdatedAtDate: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: LastUpdatedAtDate) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> LastUpdatedAtDate:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
