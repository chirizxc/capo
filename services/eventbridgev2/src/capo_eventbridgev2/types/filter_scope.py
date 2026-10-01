"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#FilterScope``."""

from typing import Literal, TypeAlias, cast

"""Scope of a filter pattern within a FilterConfiguration."""
FilterScope: TypeAlias = Literal[
    "DATA",
    "METADATA",
    "SYSTEM_METADATA",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FilterScope) -> str:
    return value


def deserialize_cbor(data: str) -> FilterScope:
    return cast(FilterScope, data)
