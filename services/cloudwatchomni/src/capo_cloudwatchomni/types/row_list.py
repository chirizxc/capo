"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#RowList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.row

RowList: TypeAlias = list["capo_cloudwatchomni.types.row.Row"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RowList) -> list:
    import capo_cloudwatchomni.types.row

    out: list = []
    for item in value:
        out.append(capo_cloudwatchomni.types.row.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> RowList:
    import capo_cloudwatchomni.types.row

    out: RowList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatchomni.types.row.deserialize_cbor(item))
    return out
