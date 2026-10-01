"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#IncludePayload``."""

from typing import Literal, TypeAlias, cast

IncludePayload: TypeAlias = Literal[
    "FULL",
    "ON_ERROR_ONLY",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IncludePayload) -> str:
    return value


def deserialize_cbor(data: str) -> IncludePayload:
    return cast(IncludePayload, data)
