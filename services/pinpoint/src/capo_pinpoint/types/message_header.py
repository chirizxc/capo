"""Generated from Smithy shape ``com.amazonaws.pinpoint#MessageHeader``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string


class MessageHeader(TypedDict, closed=True):
    name: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The name of the message header. The header name can contain up to 126 characters.</p>"""
    value: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The value of the message header. The header value can contain up to 870 characters, including the length of any rendered attributes. For example if you add the {CreationDate} attribute, it renders as YYYY-MM-DDTHH:MM:SS.SSSZ and is 24 characters in length.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageHeader) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> MessageHeader:
    out: MessageHeader = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out
