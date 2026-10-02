"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#AlertSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.alert_summary

AlertSummaryList: TypeAlias = list[
    "capo_cloudwatchomni.types.alert_summary.AlertSummary"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AlertSummaryList) -> list:
    import capo_cloudwatchomni.types.alert_summary

    out: list = []
    for item in value:
        out.append(capo_cloudwatchomni.types.alert_summary.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> AlertSummaryList:
    import capo_cloudwatchomni.types.alert_summary

    out: AlertSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatchomni.types.alert_summary.deserialize_cbor(item))
    return out
