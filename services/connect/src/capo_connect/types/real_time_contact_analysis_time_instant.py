"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisTimeInstant``."""

import datetime
from typing import TypeAlias

RealTimeContactAnalysisTimeInstant: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisTimeInstant) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def deserialize_json(data: str) -> RealTimeContactAnalysisTimeInstant:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))
