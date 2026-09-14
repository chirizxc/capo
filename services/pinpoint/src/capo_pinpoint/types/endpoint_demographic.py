"""Generated from Smithy shape ``com.amazonaws.pinpoint#EndpointDemographic``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string


class EndpointDemographic(TypedDict, closed=True):
    app_version: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The version of the app that's associated with the endpoint.</p>"""
    locale: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The locale of the endpoint, in the following format: the ISO 639-1 alpha-2 code, followed by an underscore (_), followed by an ISO 3166-1 alpha-2 value.</p>"""
    make: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The manufacturer of the endpoint device, such as apple or samsung.</p>"""
    model: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The model name or number of the endpoint device, such as iPhone or SM-G900F.</p>"""
    model_version: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The model version of the endpoint device.</p>"""
    platform: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The platform of the endpoint device, such as ios.</p>"""
    platform_version: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The platform version of the endpoint device.</p>"""
    timezone: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The time zone of the endpoint, specified as a tz database name value, such as America/Los_Angeles.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EndpointDemographic) -> dict:
    out: dict = {}
    if "app_version" in value:
        out["AppVersion"] = value["app_version"]
    if "locale" in value:
        out["Locale"] = value["locale"]
    if "make" in value:
        out["Make"] = value["make"]
    if "model" in value:
        out["Model"] = value["model"]
    if "model_version" in value:
        out["ModelVersion"] = value["model_version"]
    if "platform" in value:
        out["Platform"] = value["platform"]
    if "platform_version" in value:
        out["PlatformVersion"] = value["platform_version"]
    if "timezone" in value:
        out["Timezone"] = value["timezone"]
    return out


def deserialize_json(data: dict) -> EndpointDemographic:
    out: EndpointDemographic = {}  # type: ignore[typeddict-item]
    if data.get("AppVersion") is not None:
        out["app_version"] = data["AppVersion"]
    if data.get("Locale") is not None:
        out["locale"] = data["Locale"]
    if data.get("Make") is not None:
        out["make"] = data["Make"]
    if data.get("Model") is not None:
        out["model"] = data["Model"]
    if data.get("ModelVersion") is not None:
        out["model_version"] = data["ModelVersion"]
    if data.get("Platform") is not None:
        out["platform"] = data["Platform"]
    if data.get("PlatformVersion") is not None:
        out["platform_version"] = data["PlatformVersion"]
    if data.get("Timezone") is not None:
        out["timezone"] = data["Timezone"]
    return out
