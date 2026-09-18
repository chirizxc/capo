"""Generated from Smithy shape ``com.amazonaws.workdocs#TimestampType``."""

import datetime
from typing import TypeAlias

TimestampType: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: TimestampType) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> TimestampType:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
