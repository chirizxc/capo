"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ThresholdMode``."""

from typing import Literal, TypeAlias, cast

"""How a threshold is applied to query results."""
ThresholdMode: TypeAlias = Literal[
    "COUNT_OF_RESULTS",
    "FIELD_VALUE",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ThresholdMode) -> str:
    return value


def deserialize_cbor(data: str) -> ThresholdMode:
    return cast(ThresholdMode, data)
