"""Generated from Smithy shape ``com.amazonaws.simpledbv2#ExportDataCutoffTime``."""

import datetime
from typing import TypeAlias

ExportDataCutoffTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: ExportDataCutoffTime) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> ExportDataCutoffTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
