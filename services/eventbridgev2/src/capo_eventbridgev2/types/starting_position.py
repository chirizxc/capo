"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#StartingPosition``."""

from typing import Literal, TypeAlias, cast

"""Starting position for a subscriber."""
StartingPosition: TypeAlias = Literal[
    "LATEST",
    "POINT_IN_TIME",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartingPosition) -> str:
    return value


def deserialize_cbor(data: str) -> StartingPosition:
    return cast(StartingPosition, data)
