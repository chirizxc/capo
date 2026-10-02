"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#TraceMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.trace_metadata

TraceMetadataList: TypeAlias = list[
    "capo_cloudwatchomni.types.trace_metadata.TraceMetadata"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TraceMetadataList) -> list:
    import capo_cloudwatchomni.types.trace_metadata

    out: list = []
    for item in value:
        out.append(capo_cloudwatchomni.types.trace_metadata.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> TraceMetadataList:
    import capo_cloudwatchomni.types.trace_metadata

    out: TraceMetadataList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatchomni.types.trace_metadata.deserialize_cbor(item))
    return out
