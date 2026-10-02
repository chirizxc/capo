"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#Comparator``."""

from typing import Literal, TypeAlias, cast

"""Comparison operator for a threshold."""
Comparator: TypeAlias = Literal[
    "GT",
    "LT",
    "GTE",
    "LTE",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Comparator) -> str:
    return value


def deserialize_cbor(data: str) -> Comparator:
    return cast(Comparator, data)
