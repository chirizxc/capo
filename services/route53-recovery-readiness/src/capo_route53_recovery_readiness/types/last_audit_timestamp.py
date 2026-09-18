"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#LastAuditTimestamp``."""

import datetime
from typing import TypeAlias

"""<p>The time that a recovery group was last assessed for recommendations, in UTC ISO-8601 format.</p>"""
LastAuditTimestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: LastAuditTimestamp) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def deserialize_json(data: str) -> LastAuditTimestamp:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))
