"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#ReadinessCheckTimestamp``."""

import datetime
from typing import TypeAlias

"""<p>The time (UTC) that the cell was last checked for readiness, in ISO-8601 format.</p>"""
ReadinessCheckTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: ReadinessCheckTimestamp) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def deserialize_json(data: str) -> ReadinessCheckTimestamp:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))
