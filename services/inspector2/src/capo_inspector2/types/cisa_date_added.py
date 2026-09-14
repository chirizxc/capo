"""Generated from Smithy shape ``com.amazonaws.inspector2#CisaDateAdded``."""

import datetime
from typing import TypeAlias

CisaDateAdded: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: CisaDateAdded) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> CisaDateAdded:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
