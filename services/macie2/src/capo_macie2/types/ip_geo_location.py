"""Generated from Smithy shape ``com.amazonaws.macie2#IpGeoLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__double


class IpGeoLocation(TypedDict, closed=True):
    lat: NotRequired["capo_macie2.types.__double.__double"]
    """<p>The latitude coordinate of the location, rounded to four decimal places.</p>"""
    lon: NotRequired["capo_macie2.types.__double.__double"]
    """<p>The longitude coordinate of the location, rounded to four decimal places.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IpGeoLocation) -> dict:
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


def deserialize_json(data: dict) -> IpGeoLocation:
    out: IpGeoLocation = {}  # type: ignore[typeddict-item]
    if data.get("lat") is not None:
        out["lat"] = float(data["lat"])
    if data.get("lon") is not None:
        out["lon"] = float(data["lon"])
    return out
