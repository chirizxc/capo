"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialNullSymbolStyle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.geospatial_width
    import capo_quicksight.types.hex_color_with_transparency


class GeospatialNullSymbolStyle(TypedDict, closed=True):
    fill_color: NotRequired[
        "capo_quicksight.types.hex_color_with_transparency.HexColorWithTransparency"
    ]
    """<p>The color and opacity values for the fill color.</p>"""
    stroke_color: NotRequired[
        "capo_quicksight.types.hex_color_with_transparency.HexColorWithTransparency"
    ]
    """<p>The color and opacity values for the stroke color.</p>"""
    stroke_width: NotRequired["capo_quicksight.types.geospatial_width.GeospatialWidth"]
    """<p>The width of the border stroke.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialNullSymbolStyle) -> dict:
    out: dict = {}
    if "fill_color" in value:
        out["FillColor"] = value["fill_color"]
    if "stroke_color" in value:
        out["StrokeColor"] = value["stroke_color"]
    if "stroke_width" in value:
        out["StrokeWidth"] = (
            "NaN"
            if value["stroke_width"] != value["stroke_width"]
            else "Infinity"
            if value["stroke_width"] == float("inf")
            else "-Infinity"
            if value["stroke_width"] == float("-inf")
            else value["stroke_width"]
        )
    return out


def deserialize_json(data: dict) -> GeospatialNullSymbolStyle:
    out: GeospatialNullSymbolStyle = {}  # type: ignore[typeddict-item]
    if data.get("FillColor") is not None:
        out["fill_color"] = data["FillColor"]
    if data.get("StrokeColor") is not None:
        out["stroke_color"] = data["StrokeColor"]
    if data.get("StrokeWidth") is not None:
        out["stroke_width"] = float(data["StrokeWidth"])
    return out
