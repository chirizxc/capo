"""Generated from Smithy shape ``com.amazonaws.connect#StartContactConversationalAnalyticsJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_id
    import capo_connect.types.instance_id


class StartContactConversationalAnalyticsJobResponse(TypedDict, closed=True):
    instance_id: NotRequired["capo_connect.types.instance_id.InstanceId"]
    """<p>The identifier of the Connect Customer instance.</p>"""
    contact_id: NotRequired["capo_connect.types.contact_id.ContactId"]
    """<p>The identifier of the contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartContactConversationalAnalyticsJobResponse) -> dict:
    out: dict = {}
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "contact_id" in value:
        out["ContactId"] = value["contact_id"]
    return out


def deserialize_json(data: dict) -> StartContactConversationalAnalyticsJobResponse:
    out: StartContactConversationalAnalyticsJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    if data.get("ContactId") is not None:
        out["contact_id"] = data["ContactId"]
    return out
