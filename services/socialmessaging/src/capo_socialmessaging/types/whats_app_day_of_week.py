"""Generated from Smithy shape ``com.amazonaws.socialmessaging#WhatsAppDayOfWeek``."""

from typing import Literal, TypeAlias, cast

WhatsAppDayOfWeek: TypeAlias = Literal[
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY",
    "SUNDAY",
]


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppDayOfWeek) -> str:
    return value


def deserialize_json(data: str) -> WhatsAppDayOfWeek:
    return cast(WhatsAppDayOfWeek, data)
