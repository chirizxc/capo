"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#RowScopeOperator``."""

from typing import Literal, TypeAlias, cast

"""Match operator for a row-scope filter. Only IN is supported."""
RowScopeOperator: TypeAlias = Literal["IN",]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RowScopeOperator) -> str:
    return value


def deserialize_cbor(data: str) -> RowScopeOperator:
    return cast(RowScopeOperator, data)
