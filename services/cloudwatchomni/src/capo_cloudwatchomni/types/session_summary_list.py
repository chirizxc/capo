"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#SessionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.session_summary

SessionSummaryList: TypeAlias = list[
    "capo_cloudwatchomni.types.session_summary.SessionSummary"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SessionSummaryList) -> list:
    import capo_cloudwatchomni.types.session_summary

    out: list = []
    for item in value:
        out.append(capo_cloudwatchomni.types.session_summary.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> SessionSummaryList:
    import capo_cloudwatchomni.types.session_summary

    out: SessionSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatchomni.types.session_summary.deserialize_cbor(item))
    return out
