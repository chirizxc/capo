"""Generated from Smithy shape ``com.amazonaws.connect#AvailableFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.available_filter_type
    import capo_connect.types.filter_id


class AvailableFilter(TypedDict, closed=True):
    id: NotRequired["capo_connect.types.filter_id.FilterId"]
    """<p>The identifier of the filter.</p>"""
    type: NotRequired["capo_connect.types.available_filter_type.AvailableFilterType"]
    """<p>The type of the filter. Valid values: <code>METRIC_LEVEL</code> | <code>RESOURCE_LEVEL</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AvailableFilter) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "type" in value:
        import capo_connect.types.available_filter_type

        out["Type"] = capo_connect.types.available_filter_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> AvailableFilter:
    out: AvailableFilter = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Type") is not None:
        import capo_connect.types.available_filter_type

        out["type"] = capo_connect.types.available_filter_type.deserialize_json(
            data["Type"]
        )
    return out
