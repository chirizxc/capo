"""Generated from Smithy shape ``com.amazonaws.securityhub#GeoLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.double


class GeoLocation(TypedDict, closed=True):
    lon: NotRequired["capo_securityhub.types.double.Double"]
    """<p>The longitude of the location.</p>"""
    lat: NotRequired["capo_securityhub.types.double.Double"]
    """<p>The latitude of the location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeoLocation) -> dict:
    out: dict = {}
    if "lon" in value:
        out["Lon"] = (
            "NaN"
            if value["lon"] != value["lon"]
            else "Infinity"
            if value["lon"] == float("inf")
            else "-Infinity"
            if value["lon"] == float("-inf")
            else value["lon"]
        )
    if "lat" in value:
        out["Lat"] = (
            "NaN"
            if value["lat"] != value["lat"]
            else "Infinity"
            if value["lat"] == float("inf")
            else "-Infinity"
            if value["lat"] == float("-inf")
            else value["lat"]
        )
    return out


def deserialize_json(data: dict) -> GeoLocation:
    out: GeoLocation = {}  # type: ignore[typeddict-item]
    if data.get("Lon") is not None:
        out["lon"] = float(data["Lon"])
    if data.get("Lat") is not None:
        out["lat"] = float(data["Lat"])
    return out
