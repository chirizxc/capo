"""Generated from Smithy shape ``com.amazonaws.dsql#StreamCreationTime``."""

import datetime
from typing import TypeAlias

"""<p>The timestamp when the stream was created.</p>"""
StreamCreationTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: StreamCreationTime) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> StreamCreationTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
