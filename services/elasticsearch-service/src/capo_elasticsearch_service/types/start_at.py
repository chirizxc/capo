"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#StartAt``."""

import datetime
from typing import TypeAlias

StartAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: StartAt) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> StartAt:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
