"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#LogMetadataAttributeMap``."""

from typing import TypeAlias

LogMetadataAttributeMap: TypeAlias = dict["str", "str"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: LogMetadataAttributeMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_cbor(data: dict) -> LogMetadataAttributeMap:
    out: LogMetadataAttributeMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
