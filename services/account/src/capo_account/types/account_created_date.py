"""Generated from Smithy shape ``com.amazonaws.account#AccountCreatedDate``."""

import datetime
from typing import TypeAlias

AccountCreatedDate: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: AccountCreatedDate) -> str:
    value = (
        value.astimezone(datetime.timezone.utc)
        if value.tzinfo
        else value.replace(tzinfo=datetime.timezone.utc)
    )
    return value.isoformat().replace("+00:00", "Z")


def deserialize_json(data: str) -> AccountCreatedDate:
    return datetime.datetime.fromisoformat(data.replace("Z", "+00:00"))
