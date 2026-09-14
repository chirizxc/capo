"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialLineWidth``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.geospatial_width


class GeospatialLineWidth(TypedDict, closed=True):
    line_width: NotRequired["capo_quicksight.types.geospatial_width.GeospatialWidth"]
    """<p>The positive value for the width of a line.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialLineWidth) -> dict:
    out: dict = {}
    if "line_width" in value:
        out["LineWidth"] = (
            "NaN"
            if value["line_width"] != value["line_width"]
            else "Infinity"
            if value["line_width"] == float("inf")
            else "-Infinity"
            if value["line_width"] == float("-inf")
            else value["line_width"]
        )
    return out


def deserialize_json(data: dict) -> GeospatialLineWidth:
    out: GeospatialLineWidth = {}  # type: ignore[typeddict-item]
    if data.get("LineWidth") is not None:
        out["line_width"] = float(data["LineWidth"])
    return out
