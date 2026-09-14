"""Generated from Smithy shape ``com.amazonaws.omics#WorkflowTimestamp``."""

import datetime
from typing import TypeAlias

WorkflowTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowTimestamp) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def deserialize_json(data: str) -> WorkflowTimestamp:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))
