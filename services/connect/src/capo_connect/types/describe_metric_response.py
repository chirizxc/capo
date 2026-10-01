"""Generated from Smithy shape ``com.amazonaws.connect#DescribeMetricResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.metric_definition


class DescribeMetricResponse(TypedDict, closed=True):
    metric: "capo_connect.types.metric_definition.MetricDefinition"
    """<p>The metric definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeMetricResponse) -> dict:
    out: dict = {}
    import capo_connect.types.metric_definition

    out["Metric"] = capo_connect.types.metric_definition.serialize_json(value["metric"])
    return out


def deserialize_json(data: dict) -> DescribeMetricResponse:
    out: DescribeMetricResponse = {}  # type: ignore[typeddict-item]
    if data.get("Metric") is not None:
        import capo_connect.types.metric_definition

        out["metric"] = capo_connect.types.metric_definition.deserialize_json(
            data["Metric"]
        )
    else:
        raise DeserializationError("DescribeMetricResponse.metric required")
    return out
