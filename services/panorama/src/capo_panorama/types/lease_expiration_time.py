"""Generated from Smithy shape ``com.amazonaws.panorama#LeaseExpirationTime``."""

import datetime
from typing import TypeAlias

LeaseExpirationTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: LeaseExpirationTime) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> LeaseExpirationTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
