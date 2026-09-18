"""Generated from Smithy shape ``com.amazonaws.amplify#webhookCreateTime``."""

import datetime
from typing import TypeAlias

webhookCreateTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: webhookCreateTime) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> webhookCreateTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
