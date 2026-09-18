"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#TimeStamp``."""

import datetime
from typing import TypeAlias

"""Timestamp with no UTC offset or timezone"""
TimeStamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: TimeStamp) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def deserialize_json(data: str) -> TimeStamp:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))
