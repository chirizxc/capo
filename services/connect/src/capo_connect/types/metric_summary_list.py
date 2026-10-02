"""Generated from Smithy shape ``com.amazonaws.connect#MetricSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.metric_summary

MetricSummaryList: TypeAlias = list["capo_connect.types.metric_summary.MetricSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: MetricSummaryList) -> list:
    import capo_connect.types.metric_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.metric_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetricSummaryList:
    import capo_connect.types.metric_summary

    out: MetricSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connect.types.metric_summary.deserialize_json(item))
    return out
