"""Generated from Smithy shape ``com.amazonaws.medialive#__timestamp``."""

import datetime
from typing import TypeAlias

"""Placeholder documentation for __timestamp"""
__timestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: __timestamp) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> __timestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
