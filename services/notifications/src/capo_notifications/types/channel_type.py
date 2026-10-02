"""Generated from Smithy shape ``com.amazonaws.notifications#ChannelType``."""

from typing import Literal, TypeAlias, cast

ChannelType: TypeAlias = Literal[
    "MOBILE",
    "CHATBOT",
    "EMAIL",
    "ACCOUNT_CONTACT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelType) -> str:
    return value


def deserialize_json(data: str) -> ChannelType:
    return cast(ChannelType, data)
