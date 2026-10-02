"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#NotificationTargetType``."""

from typing import Literal, TypeAlias, cast

"""Supported notification target type."""
NotificationTargetType: TypeAlias = Literal[
    "sns",
    "slack",
    "pagerduty",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NotificationTargetType) -> str:
    return value


def deserialize_cbor(data: str) -> NotificationTargetType:
    return cast(NotificationTargetType, data)
