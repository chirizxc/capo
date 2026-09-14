"""Generated from Smithy shape ``com.amazonaws.ebs#TimeStamp``."""

import datetime
from typing import TypeAlias

TimeStamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: TimeStamp) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> TimeStamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
