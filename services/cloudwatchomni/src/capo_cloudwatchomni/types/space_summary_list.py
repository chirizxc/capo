"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#SpaceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.space_summary

SpaceSummaryList: TypeAlias = list[
    "capo_cloudwatchomni.types.space_summary.SpaceSummary"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SpaceSummaryList) -> list:
    import capo_cloudwatchomni.types.space_summary

    out: list = []
    for item in value:
        out.append(capo_cloudwatchomni.types.space_summary.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> SpaceSummaryList:
    import capo_cloudwatchomni.types.space_summary

    out: SpaceSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatchomni.types.space_summary.deserialize_cbor(item))
    return out
