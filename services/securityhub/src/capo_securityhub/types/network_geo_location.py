"""Generated from Smithy shape ``com.amazonaws.securityhub#NetworkGeoLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.double
    import capo_securityhub.types.non_empty_string


class NetworkGeoLocation(TypedDict, closed=True):
    city: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the city. </p>"""
    country: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the country. </p>"""
    lat: NotRequired["capo_securityhub.types.double.Double"]
    """<p> The latitude information of the endpoint location. </p>"""
    lon: NotRequired["capo_securityhub.types.double.Double"]
    """<p> The longitude information of the endpoint location. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkGeoLocation) -> dict:
    out: dict = {}
    if "city" in value:
        out["City"] = value["city"]
    if "country" in value:
        out["Country"] = value["country"]
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
    return out


def deserialize_json(data: dict) -> NetworkGeoLocation:
    out: NetworkGeoLocation = {}  # type: ignore[typeddict-item]
    if data.get("City") is not None:
        out["city"] = data["City"]
    if data.get("Country") is not None:
        out["country"] = data["Country"]
    if data.get("Lat") is not None:
        out["lat"] = float(data["Lat"])
    if data.get("Lon") is not None:
        out["lon"] = float(data["Lon"])
    return out
