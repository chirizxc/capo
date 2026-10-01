"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ResourceScopeTagMap``."""

from typing import TypeAlias

ResourceScopeTagMap: TypeAlias = dict["str", "str"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: ResourceScopeTagMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_cbor(data: dict) -> ResourceScopeTagMap:
    out: ResourceScopeTagMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
