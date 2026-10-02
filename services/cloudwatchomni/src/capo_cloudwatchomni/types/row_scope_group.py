"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#RowScopeGroup``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.row_scope

RowScopeGroup: TypeAlias = list["capo_cloudwatchomni.types.row_scope.RowScope"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RowScopeGroup) -> list:
    import capo_cloudwatchomni.types.row_scope

    out: list = []
    for item in value:
        out.append(capo_cloudwatchomni.types.row_scope.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> RowScopeGroup:
    import capo_cloudwatchomni.types.row_scope

    out: RowScopeGroup = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatchomni.types.row_scope.deserialize_cbor(item))
    return out
