"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#TagMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.tag_key
    import capo_cloudwatchomni.types.tag_value

TagMap: TypeAlias = dict[
    "capo_cloudwatchomni.types.tag_key.TagKey",
    "capo_cloudwatchomni.types.tag_value.TagValue",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: TagMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_cbor(data: dict) -> TagMap:
    out: TagMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
