"""Generated from Smithy shape ``com.amazonaws.mpa#IsoTimestamp``."""

import datetime
from typing import TypeAlias

IsoTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: IsoTimestamp) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def deserialize_json(data: str) -> IsoTimestamp:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))
