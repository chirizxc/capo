"""Generated from Smithy shape ``com.amazonaws.guardduty#GeoLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.double


class GeoLocation(TypedDict, closed=True):
    lat: NotRequired["capo_guardduty.types.double.Double"]
    """<p>The latitude information of the remote IP address.</p>"""
    lon: NotRequired["capo_guardduty.types.double.Double"]
    """<p>The longitude information of the remote IP address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeoLocation) -> dict:
    out: dict = {}
    if "lat" in value:
        out["lat"] = (
            "NaN"
            if value["lat"] != value["lat"]
            else "Infinity"
            if value["lat"] == float("inf")
            else "-Infinity"
            if value["lat"] == float("-inf")
            else value["lat"]
        )
    if "lon" in value:
        out["lon"] = (
            "NaN"
            if value["lon"] != value["lon"]
            else "Infinity"
            if value["lon"] == float("inf")
            else "-Infinity"
            if value["lon"] == float("-inf")
            else value["lon"]
        )
    return out


def deserialize_json(data: dict) -> GeoLocation:
    out: GeoLocation = {}  # type: ignore[typeddict-item]
    if data.get("lat") is not None:
        out["lat"] = float(data["lat"])
    if data.get("lon") is not None:
        out["lon"] = float(data["lon"])
    return out
