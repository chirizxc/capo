"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#SetupAt``."""

import datetime
from typing import TypeAlias

SetupAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: SetupAt) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> SetupAt:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
