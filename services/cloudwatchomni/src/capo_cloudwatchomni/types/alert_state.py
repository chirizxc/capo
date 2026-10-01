"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#AlertState``."""

from typing import Literal, TypeAlias, cast

"""Flat alert state. Severity is folded in: a WARNING/CRITICAL alert reports that state directly. {@code NODATA} indicates the evaluation produced no data (subject to the rule's noData.treatAs handling)."""
AlertState: TypeAlias = Literal[
    "OK",
    "WARNING",
    "CRITICAL",
    "NODATA",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AlertState) -> str:
    return value


def deserialize_cbor(data: str) -> AlertState:
    return cast(AlertState, data)
