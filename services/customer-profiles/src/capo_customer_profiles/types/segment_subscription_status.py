"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SegmentSubscriptionStatus``."""

from typing import Literal, TypeAlias, cast

SegmentSubscriptionStatus: TypeAlias = Literal[
    "STARTING",
    "RUNNING",
    "STOPPED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SegmentSubscriptionStatus) -> str:
    return value


def deserialize_json(data: str) -> SegmentSubscriptionStatus:
    return cast(SegmentSubscriptionStatus, data)
