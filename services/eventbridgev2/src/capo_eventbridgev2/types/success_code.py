"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#SuccessCode``."""

from typing import Literal, TypeAlias, cast

"""Indicates the outcome for a successfully processed publish entry."""
SuccessCode: TypeAlias = Literal[
    "PUBLISHED",
    "DEDUPLICATED",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SuccessCode) -> str:
    return value


def deserialize_cbor(data: str) -> SuccessCode:
    return cast(SuccessCode, data)
