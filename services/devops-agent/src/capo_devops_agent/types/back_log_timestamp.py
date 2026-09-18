"""Generated from Smithy shape ``com.amazonaws.devopsagent#BackLogTimestamp``."""

import datetime
from typing import TypeAlias

"""<p>Timestamp format used for backlog operations</p>"""
BackLogTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: BackLogTimestamp) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def deserialize_json(data: str) -> BackLogTimestamp:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))
