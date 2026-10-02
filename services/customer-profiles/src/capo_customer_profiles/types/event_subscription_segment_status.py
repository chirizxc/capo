"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EventSubscriptionSegmentStatus``."""

from typing import Literal, TypeAlias, cast

EventSubscriptionSegmentStatus: TypeAlias = Literal[
    "STARTING",
    "RUNNING",
    "STOPPED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EventSubscriptionSegmentStatus) -> str:
    return value


def deserialize_json(data: str) -> EventSubscriptionSegmentStatus:
    return cast(EventSubscriptionSegmentStatus, data)
