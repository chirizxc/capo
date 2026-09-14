"""Generated from Smithy shape ``com.amazonaws.pinpoint#GPSCoordinates``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__double


class GPSCoordinates(TypedDict, closed=True):
    latitude: NotRequired["capo_pinpoint.types.__double.__double"]
    """<p>The latitude coordinate of the location.</p>"""
    longitude: NotRequired["capo_pinpoint.types.__double.__double"]
    """<p>The longitude coordinate of the location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GPSCoordinates) -> dict:
    out: dict = {}
    if "latitude" in value:
        out["Latitude"] = (
            "NaN"
            if value["latitude"] != value["latitude"]
            else "Infinity"
            if value["latitude"] == float("inf")
            else "-Infinity"
            if value["latitude"] == float("-inf")
            else value["latitude"]
        )
    if "longitude" in value:
        out["Longitude"] = (
            "NaN"
            if value["longitude"] != value["longitude"]
            else "Infinity"
            if value["longitude"] == float("inf")
            else "-Infinity"
            if value["longitude"] == float("-inf")
            else value["longitude"]
        )
    return out


def deserialize_json(data: dict) -> GPSCoordinates:
    out: GPSCoordinates = {}  # type: ignore[typeddict-item]
    if data.get("Latitude") is not None:
        out["latitude"] = float(data["Latitude"])
    if data.get("Longitude") is not None:
        out["longitude"] = float(data["Longitude"])
    return out
