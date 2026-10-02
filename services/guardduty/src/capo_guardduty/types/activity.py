"""Generated from Smithy shape ``com.amazonaws.guardduty#Activity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.activity_type
    import capo_guardduty.types.api_call


class Activity(TypedDict, closed=True):
    type: NotRequired["capo_guardduty.types.activity_type.ActivityType"]
    """<p>The type of the observed activity.</p>"""
    api: NotRequired["capo_guardduty.types.api_call.ApiCall"]
    """<p>Contains information about the API call that was observed, when the activity type is <code>API_CALL</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Activity) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_guardduty.types.activity_type

        out["type"] = capo_guardduty.types.activity_type.serialize_json(value["type"])
    if "api" in value:
        import capo_guardduty.types.api_call

        out["api"] = capo_guardduty.types.api_call.serialize_json(value["api"])
    return out


def deserialize_json(data: dict) -> Activity:
    out: Activity = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_guardduty.types.activity_type

        out["type"] = capo_guardduty.types.activity_type.deserialize_json(data["type"])
    if data.get("api") is not None:
        import capo_guardduty.types.api_call

        out["api"] = capo_guardduty.types.api_call.deserialize_json(data["api"])
    return out
