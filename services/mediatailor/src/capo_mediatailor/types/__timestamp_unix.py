"""Generated from Smithy shape ``com.amazonaws.mediatailor#__timestampUnix``."""

import datetime
from typing import TypeAlias

__timestampUnix: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: __timestampUnix) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> __timestampUnix:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
