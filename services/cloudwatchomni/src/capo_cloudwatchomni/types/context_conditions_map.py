"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ContextConditionsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.string_list

ContextConditionsMap: TypeAlias = dict[
    "str", "capo_cloudwatchomni.types.string_list.StringList"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: ContextConditionsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_cloudwatchomni.types.string_list

        out[key] = capo_cloudwatchomni.types.string_list.serialize_cbor(value)
    return out


def deserialize_cbor(data: dict) -> ContextConditionsMap:
    out: ContextConditionsMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_cloudwatchomni.types.string_list

        out[key] = capo_cloudwatchomni.types.string_list.deserialize_cbor(value)
    return out
