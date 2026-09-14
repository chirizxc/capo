"""Generated from Smithy shape ``com.amazonaws.iotwireless#Accuracy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.horizontal_accuracy
    import capo_iot_wireless.types.vertical_accuracy


class Accuracy(TypedDict, closed=True):
    horizontal_accuracy: NotRequired[
        "capo_iot_wireless.types.horizontal_accuracy.HorizontalAccuracy"
    ]
    """<p>The horizontal accuracy of the estimated position, which is the difference between the estimated location and the actual device location.</p>"""
    vertical_accuracy: NotRequired[
        "capo_iot_wireless.types.vertical_accuracy.VerticalAccuracy"
    ]
    """<p>The vertical accuracy of the estimated position, which is the difference between the estimated altitude and actual device latitude in meters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Accuracy) -> dict:
    out: dict = {}
    if "horizontal_accuracy" in value:
        out["HorizontalAccuracy"] = (
            "NaN"
            if value["horizontal_accuracy"] != value["horizontal_accuracy"]
            else "Infinity"
            if value["horizontal_accuracy"] == float("inf")
            else "-Infinity"
            if value["horizontal_accuracy"] == float("-inf")
            else value["horizontal_accuracy"]
        )
    if "vertical_accuracy" in value:
        out["VerticalAccuracy"] = (
            "NaN"
            if value["vertical_accuracy"] != value["vertical_accuracy"]
            else "Infinity"
            if value["vertical_accuracy"] == float("inf")
            else "-Infinity"
            if value["vertical_accuracy"] == float("-inf")
            else value["vertical_accuracy"]
        )
    return out


def deserialize_json(data: dict) -> Accuracy:
    out: Accuracy = {}  # type: ignore[typeddict-item]
    if data.get("HorizontalAccuracy") is not None:
        out["horizontal_accuracy"] = float(data["HorizontalAccuracy"])
    if data.get("VerticalAccuracy") is not None:
        out["vertical_accuracy"] = float(data["VerticalAccuracy"])
    return out
