"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SubscriptionEventType``."""

from typing import Literal, TypeAlias, cast

SubscriptionEventType: TypeAlias = Literal[
    "LIVE",
    "SCHEDULE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionEventType) -> str:
    return value


def deserialize_json(data: str) -> SubscriptionEventType:
    return cast(SubscriptionEventType, data)
