"""Generated from Smithy shape ``com.amazonaws.quicksight#GaugeChartColorConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.hex_color


class GaugeChartColorConfiguration(TypedDict, closed=True):
    foreground_color: NotRequired["capo_quicksight.types.hex_color.HexColor"]
    """<p>The foreground color configuration of a <code>GaugeChartVisual</code>.</p>"""
    background_color: NotRequired["capo_quicksight.types.hex_color.HexColor"]
    """<p>The background color configuration of a <code>GaugeChartVisual</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GaugeChartColorConfiguration) -> dict:
    out: dict = {}
    if "foreground_color" in value:
        out["ForegroundColor"] = value["foreground_color"]
    if "background_color" in value:
        out["BackgroundColor"] = value["background_color"]
    return out


def deserialize_json(data: dict) -> GaugeChartColorConfiguration:
    out: GaugeChartColorConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ForegroundColor") is not None:
        out["foreground_color"] = data["ForegroundColor"]
    if data.get("BackgroundColor") is not None:
        out["background_color"] = data["BackgroundColor"]
    return out
