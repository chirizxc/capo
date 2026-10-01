"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EventSubscriptionState``."""

from typing import Literal, TypeAlias, cast

EventSubscriptionState: TypeAlias = Literal[
    "RUNNING",
    "UNHEALTHY",
    "STOPPED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EventSubscriptionState) -> str:
    return value


def deserialize_json(data: str) -> EventSubscriptionState:
    return cast(EventSubscriptionState, data)
