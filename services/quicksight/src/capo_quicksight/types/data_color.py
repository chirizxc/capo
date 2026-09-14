"""Generated from Smithy shape ``com.amazonaws.quicksight#DataColor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.double
    import capo_quicksight.types.hex_color


class DataColor(TypedDict, closed=True):
    color: NotRequired["capo_quicksight.types.hex_color.HexColor"]
    """<p>The color that is applied to the data value.</p>"""
    data_value: NotRequired["capo_quicksight.types.double.Double"]
    """<p>The data value that the color is applied to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataColor) -> dict:
    out: dict = {}
    if "color" in value:
        out["Color"] = value["color"]
    if "data_value" in value:
        out["DataValue"] = (
            "NaN"
            if value["data_value"] != value["data_value"]
            else "Infinity"
            if value["data_value"] == float("inf")
            else "-Infinity"
            if value["data_value"] == float("-inf")
            else value["data_value"]
        )
    return out


def deserialize_json(data: dict) -> DataColor:
    out: DataColor = {}  # type: ignore[typeddict-item]
    if data.get("Color") is not None:
        out["color"] = data["Color"]
    if data.get("DataValue") is not None:
        out["data_value"] = float(data["DataValue"])
    return out
