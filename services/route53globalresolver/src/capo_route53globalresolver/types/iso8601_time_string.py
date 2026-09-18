"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ISO8601TimeString``."""

import datetime
from typing import TypeAlias

ISO8601TimeString: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: ISO8601TimeString) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def deserialize_json(data: str) -> ISO8601TimeString:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))
