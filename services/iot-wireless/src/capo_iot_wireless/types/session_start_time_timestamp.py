"""Generated from Smithy shape ``com.amazonaws.iotwireless#SessionStartTimeTimestamp``."""

import datetime
from typing import TypeAlias

"""<p>Timestamp of when the multicast group session is to start.</p>"""
SessionStartTimeTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: SessionStartTimeTimestamp) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def deserialize_json(data: str) -> SessionStartTimeTimestamp:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))
