"""Generated from Smithy shape ``com.amazonaws.iot#CreatedAtDate``."""

import datetime
from typing import TypeAlias

CreatedAtDate: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: CreatedAtDate) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> CreatedAtDate:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
