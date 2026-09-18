"""Generated from Smithy shape ``com.amazonaws.inspector2#VendorUpdatedAt``."""

import datetime
from typing import TypeAlias

VendorUpdatedAt: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: VendorUpdatedAt) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> VendorUpdatedAt:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
