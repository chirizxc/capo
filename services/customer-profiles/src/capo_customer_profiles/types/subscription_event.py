"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SubscriptionEvent``."""

from typing import Literal, TypeAlias, cast

SubscriptionEvent: TypeAlias = Literal[
    "JOINED",
    "LEFT",
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionEvent) -> str:
    return value


def deserialize_json(data: str) -> SubscriptionEvent:
    return cast(SubscriptionEvent, data)
