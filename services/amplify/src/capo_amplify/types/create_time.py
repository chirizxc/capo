"""Generated from Smithy shape ``com.amazonaws.amplify#CreateTime``."""

import datetime
from typing import TypeAlias

CreateTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: CreateTime) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> CreateTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
