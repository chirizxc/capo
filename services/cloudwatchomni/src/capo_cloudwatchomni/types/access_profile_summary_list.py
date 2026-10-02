"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#AccessProfileSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.access_profile_summary

AccessProfileSummaryList: TypeAlias = list[
    "capo_cloudwatchomni.types.access_profile_summary.AccessProfileSummary"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccessProfileSummaryList) -> list:
    import capo_cloudwatchomni.types.access_profile_summary

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatchomni.types.access_profile_summary.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> AccessProfileSummaryList:
    import capo_cloudwatchomni.types.access_profile_summary

    out: AccessProfileSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatchomni.types.access_profile_summary.deserialize_cbor(item)
        )
    return out
