"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#FieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.field

FieldList: TypeAlias = list["capo_cloudwatchomni.types.field.Field"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FieldList) -> list:
    import capo_cloudwatchomni.types.field

    out: list = []
    for item in value:
        out.append(capo_cloudwatchomni.types.field.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> FieldList:
    import capo_cloudwatchomni.types.field

    out: FieldList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatchomni.types.field.deserialize_cbor(item))
    return out
