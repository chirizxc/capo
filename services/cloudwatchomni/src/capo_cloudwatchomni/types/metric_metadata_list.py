"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#MetricMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.metric_metadata

MetricMetadataList: TypeAlias = list[
    "capo_cloudwatchomni.types.metric_metadata.MetricMetadata"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricMetadataList) -> list:
    import capo_cloudwatchomni.types.metric_metadata

    out: list = []
    for item in value:
        out.append(capo_cloudwatchomni.types.metric_metadata.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> MetricMetadataList:
    import capo_cloudwatchomni.types.metric_metadata

    out: MetricMetadataList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatchomni.types.metric_metadata.deserialize_cbor(item))
    return out
