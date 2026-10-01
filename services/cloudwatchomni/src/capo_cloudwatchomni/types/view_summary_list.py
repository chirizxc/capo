"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ViewSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.view_summary

ViewSummaryList: TypeAlias = list["capo_cloudwatchomni.types.view_summary.ViewSummary"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ViewSummaryList) -> list:
    import capo_cloudwatchomni.types.view_summary

    out: list = []
    for item in value:
        out.append(capo_cloudwatchomni.types.view_summary.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ViewSummaryList:
    import capo_cloudwatchomni.types.view_summary

    out: ViewSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatchomni.types.view_summary.deserialize_cbor(item))
    return out
