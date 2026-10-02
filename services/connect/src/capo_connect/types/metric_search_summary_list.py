"""Generated from Smithy shape ``com.amazonaws.connect#MetricSearchSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.metric_definition

MetricSearchSummaryList: TypeAlias = list[
    "capo_connect.types.metric_definition.MetricDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricSearchSummaryList) -> list:
    import capo_connect.types.metric_definition

    out: list = []
    for item in value:
        out.append(capo_connect.types.metric_definition.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetricSearchSummaryList:
    import capo_connect.types.metric_definition

    out: MetricSearchSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connect.types.metric_definition.deserialize_json(item))
    return out
