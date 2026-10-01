"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ViewType``."""

from typing import Literal, TypeAlias, cast

"""The ownership category of a view."""
ViewType: TypeAlias = Literal[
    "USER",
    "MANAGED",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ViewType) -> str:
    return value


def deserialize_cbor(data: str) -> ViewType:
    return cast(ViewType, data)
