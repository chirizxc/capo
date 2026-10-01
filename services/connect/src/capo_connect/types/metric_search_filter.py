"""Generated from Smithy shape ``com.amazonaws.connect#MetricSearchFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.control_plane_tag_filter


class MetricSearchFilter(TypedDict, closed=True):
    tag_filter: NotRequired[
        "capo_connect.types.control_plane_tag_filter.ControlPlaneTagFilter"
    ]
    """<p>An object that can be used to specify tag conditions inside the <code>SearchFilter</code>. This accepts an OR of AND (List of List) input where:</p> <ul> <li> <p>The top level list specifies conditions that need to be applied with OR operator.</p> </li> <li> <p>The inner list specifies conditions that need to be applied with AND operator.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricSearchFilter) -> dict:
    out: dict = {}
    if "tag_filter" in value:
        import capo_connect.types.control_plane_tag_filter

        out["TagFilter"] = capo_connect.types.control_plane_tag_filter.serialize_json(
            value["tag_filter"]
        )
    return out


def deserialize_json(data: dict) -> MetricSearchFilter:
    out: MetricSearchFilter = {}  # type: ignore[typeddict-item]
    if data.get("TagFilter") is not None:
        import capo_connect.types.control_plane_tag_filter

        out["tag_filter"] = (
            capo_connect.types.control_plane_tag_filter.deserialize_json(
                data["TagFilter"]
            )
        )
    return out
