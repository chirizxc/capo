"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#NotificationTargetMetadata``."""

from typing import TypeAlias

NotificationTargetMetadata: TypeAlias = dict["str", "str"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: NotificationTargetMetadata) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_cbor(data: dict) -> NotificationTargetMetadata:
    out: NotificationTargetMetadata = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
