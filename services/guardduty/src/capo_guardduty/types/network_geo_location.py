"""Generated from Smithy shape ``com.amazonaws.guardduty#NetworkGeoLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.double
    import capo_guardduty.types.string


class NetworkGeoLocation(TypedDict, closed=True):
    city: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the city.</p>"""
    country: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the country.</p>"""
    latitude: NotRequired["capo_guardduty.types.double.Double"]
    """<p>The latitude information of the endpoint location.</p>"""
    longitude: NotRequired["capo_guardduty.types.double.Double"]
    """<p>The longitude information of the endpoint location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkGeoLocation) -> dict:
    out: dict = {}
    if "city" in value:
        out["city"] = value["city"]
    if "country" in value:
        out["country"] = value["country"]
    if "latitude" in value:
        out["lat"] = (
            "NaN"
            if value["latitude"] != value["latitude"]
            else "Infinity"
            if value["latitude"] == float("inf")
            else "-Infinity"
            if value["latitude"] == float("-inf")
            else value["latitude"]
        )
    if "longitude" in value:
        out["lon"] = (
            "NaN"
            if value["longitude"] != value["longitude"]
            else "Infinity"
            if value["longitude"] == float("inf")
            else "-Infinity"
            if value["longitude"] == float("-inf")
            else value["longitude"]
        )
    return out


def deserialize_json(data: dict) -> NetworkGeoLocation:
    out: NetworkGeoLocation = {}  # type: ignore[typeddict-item]
    if data.get("city") is not None:
        out["city"] = data["city"]
    if data.get("country") is not None:
        out["country"] = data["country"]
    if data.get("lat") is not None:
        out["latitude"] = float(data["lat"])
    if data.get("lon") is not None:
        out["longitude"] = float(data["lon"])
    return out
