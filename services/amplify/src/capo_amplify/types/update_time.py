"""Generated from Smithy shape ``com.amazonaws.amplify#UpdateTime``."""

import datetime
from typing import TypeAlias

UpdateTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTime) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> UpdateTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
