"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#OmniDashboardSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.omni_dashboard_summary

OmniDashboardSummaryList: TypeAlias = list[
    "capo_cloudwatchomni.types.omni_dashboard_summary.OmniDashboardSummary"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OmniDashboardSummaryList) -> list:
    import capo_cloudwatchomni.types.omni_dashboard_summary

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatchomni.types.omni_dashboard_summary.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> OmniDashboardSummaryList:
    import capo_cloudwatchomni.types.omni_dashboard_summary

    out: OmniDashboardSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatchomni.types.omni_dashboard_summary.deserialize_cbor(item)
        )
    return out
