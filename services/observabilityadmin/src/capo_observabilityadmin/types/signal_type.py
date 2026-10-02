"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#SignalType``."""

from typing import Literal, TypeAlias, cast

SignalType: TypeAlias = Literal[
    "LOG",
    "METRIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: SignalType) -> str:
    return value


def deserialize_json(data: str) -> SignalType:
    return cast(SignalType, data)
