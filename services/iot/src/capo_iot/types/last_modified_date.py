"""Generated from Smithy shape ``com.amazonaws.iot#LastModifiedDate``."""

import datetime
from typing import TypeAlias

LastModifiedDate: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: LastModifiedDate) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> LastModifiedDate:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
