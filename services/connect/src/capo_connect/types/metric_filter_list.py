"""Generated from Smithy shape ``com.amazonaws.connect#MetricFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.metric_filter

MetricFilterList: TypeAlias = list["capo_connect.types.metric_filter.MetricFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: MetricFilterList) -> list:
    import capo_connect.types.metric_filter

    out: list = []
    for item in value:
        out.append(capo_connect.types.metric_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetricFilterList:
    import capo_connect.types.metric_filter

    out: MetricFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connect.types.metric_filter.deserialize_json(item))
    return out
