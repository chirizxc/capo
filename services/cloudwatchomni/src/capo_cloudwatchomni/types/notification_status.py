"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#NotificationStatus``."""

from typing import Literal, TypeAlias, cast

NotificationStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NotificationStatus) -> str:
    return value


def deserialize_cbor(data: str) -> NotificationStatus:
    return cast(NotificationStatus, data)
