"""Generated from Smithy shape ``com.amazonaws.guardduty#ApiCall``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class ApiCall(TypedDict, closed=True):
    operation: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the API operation that was invoked.</p>"""
    service: NotRequired["capo_guardduty.types.string.String"]
    """<p>The service that the API operation was invoked against.</p>"""
    error: NotRequired["capo_guardduty.types.string.String"]
    """<p>The error code that was returned, if the API call failed.</p>"""
    user_agent: NotRequired["capo_guardduty.types.string.String"]
    """<p>User agent in the request to the API operation</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiCall) -> dict:
    out: dict = {}
    if "operation" in value:
        out["operation"] = value["operation"]
    if "service" in value:
        out["service"] = value["service"]
    if "error" in value:
        out["error"] = value["error"]
    if "user_agent" in value:
        out["userAgent"] = value["user_agent"]
    return out


def deserialize_json(data: dict) -> ApiCall:
    out: ApiCall = {}  # type: ignore[typeddict-item]
    if data.get("operation") is not None:
        out["operation"] = data["operation"]
    if data.get("service") is not None:
        out["service"] = data["service"]
    if data.get("error") is not None:
        out["error"] = data["error"]
    if data.get("userAgent") is not None:
        out["user_agent"] = data["userAgent"]
    return out
