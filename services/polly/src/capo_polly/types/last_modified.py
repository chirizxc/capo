"""Generated from Smithy shape ``com.amazonaws.polly#LastModified``."""

import datetime
from typing import TypeAlias

LastModified: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: LastModified) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> LastModified:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
