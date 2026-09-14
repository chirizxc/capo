"""Generated from Smithy shape ``com.amazonaws.opensearch#UpdateTimestamp``."""

import datetime
from typing import TypeAlias

UpdateTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTimestamp) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> UpdateTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
