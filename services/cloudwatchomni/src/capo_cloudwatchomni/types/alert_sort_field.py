"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#AlertSortField``."""

from typing import Literal, TypeAlias, cast

"""Field by which alerts can be sorted."""
AlertSortField: TypeAlias = Literal[
    "NAME",
    "STATE",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AlertSortField) -> str:
    return value


def deserialize_cbor(data: str) -> AlertSortField:
    return cast(AlertSortField, data)
