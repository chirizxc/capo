"""Generated from Smithy shape ``com.amazonaws.lakeformation#LastModifiedTimestamp``."""

import datetime
from typing import TypeAlias

LastModifiedTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: LastModifiedTimestamp) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> LastModifiedTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
