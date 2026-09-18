"""Generated from Smithy shape ``com.amazonaws.amplify#StartTime``."""

import datetime
from typing import TypeAlias

StartTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: StartTime) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> StartTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
