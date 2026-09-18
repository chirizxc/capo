"""Generated from Smithy shape ``com.amazonaws.iotwireless#MetricQueryTimestamp``."""

import datetime
from typing import TypeAlias

MetricQueryTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: MetricQueryTimestamp) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> MetricQueryTimestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
