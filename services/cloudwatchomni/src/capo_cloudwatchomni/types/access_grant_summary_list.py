"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#AccessGrantSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.access_grant_summary

AccessGrantSummaryList: TypeAlias = list[
    "capo_cloudwatchomni.types.access_grant_summary.AccessGrantSummary"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccessGrantSummaryList) -> list:
    import capo_cloudwatchomni.types.access_grant_summary

    out: list = []
    for item in value:
        out.append(capo_cloudwatchomni.types.access_grant_summary.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> AccessGrantSummaryList:
    import capo_cloudwatchomni.types.access_grant_summary

    out: AccessGrantSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatchomni.types.access_grant_summary.deserialize_cbor(item)
        )
    return out
