"""Generated from Smithy shape ``com.amazonaws.connect#SendOutboundWebNotificationResponse``."""

from typing_extensions import TypedDict


class SendOutboundWebNotificationResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: SendOutboundWebNotificationResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> SendOutboundWebNotificationResponse:
    out: SendOutboundWebNotificationResponse = {}  # type: ignore[typeddict-item]
    return out
