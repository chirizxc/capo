"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#LogMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.log_metadata

LogMetadataList: TypeAlias = list["capo_cloudwatchomni.types.log_metadata.LogMetadata"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LogMetadataList) -> list:
    import capo_cloudwatchomni.types.log_metadata

    out: list = []
    for item in value:
        out.append(capo_cloudwatchomni.types.log_metadata.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> LogMetadataList:
    import capo_cloudwatchomni.types.log_metadata

    out: LogMetadataList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatchomni.types.log_metadata.deserialize_cbor(item))
    return out
