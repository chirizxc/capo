"""Generated from Smithy shape ``com.amazonaws.pinpoint#TemplateCreateMessageBody``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string


class TemplateCreateMessageBody(TypedDict, closed=True):
    arn: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the message template that was created.</p>"""
    message: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The message that's returned from the API for the request to create the message template.</p>"""
    request_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the request to create the message template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateCreateMessageBody) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "message" in value:
        out["Message"] = value["message"]
    if "request_id" in value:
        out["RequestID"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> TemplateCreateMessageBody:
    out: TemplateCreateMessageBody = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("RequestID") is not None:
        out["request_id"] = data["RequestID"]
    return out
