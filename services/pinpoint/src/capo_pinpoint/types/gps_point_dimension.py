"""Generated from Smithy shape ``com.amazonaws.pinpoint#GPSPointDimension``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__double
    import capo_pinpoint.types.gps_coordinates


class GPSPointDimension(TypedDict, closed=True):
    coordinates: NotRequired["capo_pinpoint.types.gps_coordinates.GPSCoordinates"]
    """<p>The GPS coordinates to measure distance from.</p>"""
    range_in_kilometers: NotRequired["capo_pinpoint.types.__double.__double"]
    """<p>The range, in kilometers, from the GPS coordinates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GPSPointDimension) -> dict:
    out: dict = {}
    if "coordinates" in value:
        import capo_pinpoint.types.gps_coordinates

        out["Coordinates"] = capo_pinpoint.types.gps_coordinates.serialize_json(
            value["coordinates"]
        )
    if "range_in_kilometers" in value:
        out["RangeInKilometers"] = (
            "NaN"
            if value["range_in_kilometers"] != value["range_in_kilometers"]
            else "Infinity"
            if value["range_in_kilometers"] == float("inf")
            else "-Infinity"
            if value["range_in_kilometers"] == float("-inf")
            else value["range_in_kilometers"]
        )
    return out


def deserialize_json(data: dict) -> GPSPointDimension:
    out: GPSPointDimension = {}  # type: ignore[typeddict-item]
    if data.get("Coordinates") is not None:
        import capo_pinpoint.types.gps_coordinates

        out["coordinates"] = capo_pinpoint.types.gps_coordinates.deserialize_json(
            data["Coordinates"]
        )
    if data.get("RangeInKilometers") is not None:
        out["range_in_kilometers"] = float(data["RangeInKilometers"])
    return out
