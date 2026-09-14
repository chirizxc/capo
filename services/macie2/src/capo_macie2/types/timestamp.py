"""Generated from Smithy shape ``com.amazonaws.macie2#Timestamp``."""

import datetime
from typing import TypeAlias

"""<p>Specifies a date and time in UTC and extended ISO 8601 format.</p>"""
Timestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: Timestamp) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def deserialize_json(data: str) -> Timestamp:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))
