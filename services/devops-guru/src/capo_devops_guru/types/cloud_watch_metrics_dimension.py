"""Generated from Smithy shape ``com.amazonaws.devopsguru#CloudWatchMetricsDimension``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.cloud_watch_metrics_dimension_name
    import capo_devops_guru.types.cloud_watch_metrics_dimension_value


class CloudWatchMetricsDimension(TypedDict, closed=True):
    name: NotRequired[
        "capo_devops_guru.types.cloud_watch_metrics_dimension_name.CloudWatchMetricsDimensionName"
    ]
    """<p> The name of the CloudWatch dimension. </p>"""
    value: NotRequired[
        "capo_devops_guru.types.cloud_watch_metrics_dimension_value.CloudWatchMetricsDimensionValue"
    ]
    """<p> The value of the CloudWatch dimension. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchMetricsDimension) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> CloudWatchMetricsDimension:
    out: CloudWatchMetricsDimension = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out
