"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#LogLevel``."""

from typing import Literal, TypeAlias, cast

LogLevel: TypeAlias = Literal[
    "OFF",
    "ERROR",
    "INFO",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LogLevel) -> str:
    return value


def deserialize_cbor(data: str) -> LogLevel:
    return cast(LogLevel, data)
