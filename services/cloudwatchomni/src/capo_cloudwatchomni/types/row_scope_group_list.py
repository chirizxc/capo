"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#RowScopeGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.row_scope_group

RowScopeGroupList: TypeAlias = list[
    "capo_cloudwatchomni.types.row_scope_group.RowScopeGroup"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RowScopeGroupList) -> list:
    import capo_cloudwatchomni.types.row_scope_group

    out: list = []
    for item in value:
        out.append(capo_cloudwatchomni.types.row_scope_group.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> RowScopeGroupList:
    import capo_cloudwatchomni.types.row_scope_group

    out: RowScopeGroupList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatchomni.types.row_scope_group.deserialize_cbor(item))
    return out
