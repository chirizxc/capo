"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#AlertSortOrder``."""

from typing import Literal, TypeAlias, cast

"""Sort order for list results."""
AlertSortOrder: TypeAlias = Literal[
    "ASC",
    "DESC",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AlertSortOrder) -> str:
    return value


def deserialize_cbor(data: str) -> AlertSortOrder:
    return cast(AlertSortOrder, data)
