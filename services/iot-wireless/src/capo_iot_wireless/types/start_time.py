"""Generated from Smithy shape ``com.amazonaws.iotwireless#StartTime``."""

import datetime
from typing import TypeAlias

"""<p>Start time of a FUOTA task.</p>"""
StartTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: StartTime) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def deserialize_json(data: str) -> StartTime:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))
