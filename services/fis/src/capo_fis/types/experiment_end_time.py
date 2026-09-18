"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentEndTime``."""

import datetime
from typing import TypeAlias

ExperimentEndTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentEndTime) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> ExperimentEndTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
