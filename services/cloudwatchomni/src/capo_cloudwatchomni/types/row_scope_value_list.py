"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#RowScopeValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.row_scope_value

RowScopeValueList: TypeAlias = list[
    "capo_cloudwatchomni.types.row_scope_value.RowScopeValue"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RowScopeValueList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> RowScopeValueList:
    return [item for item in data if item is not None]
