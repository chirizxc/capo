"""Generated from Smithy shape ``com.amazonaws.connect#VocabularyLastModifiedTime``."""

import datetime
from typing import TypeAlias

VocabularyLastModifiedTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: VocabularyLastModifiedTime) -> float:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.timestamp()


def deserialize_json(data: float) -> VocabularyLastModifiedTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
