"""Generated from Smithy shape ``com.amazonaws.kafka#__timestampIso8601``."""

import datetime
from typing import TypeAlias

__timestampIso8601: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: __timestampIso8601) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def deserialize_json(data: str) -> __timestampIso8601:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))
