"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#DomainSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.domain_summary

DomainSummaryList: TypeAlias = list[
    "capo_cloudwatchomni.types.domain_summary.DomainSummary"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DomainSummaryList) -> list:
    import capo_cloudwatchomni.types.domain_summary

    out: list = []
    for item in value:
        out.append(capo_cloudwatchomni.types.domain_summary.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> DomainSummaryList:
    import capo_cloudwatchomni.types.domain_summary

    out: DomainSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatchomni.types.domain_summary.deserialize_cbor(item))
    return out
