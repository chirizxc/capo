"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputMessage``."""

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError


class RouterOutputMessage(TypedDict, closed=True):
    code: "str"
    """<p>The code associated with the router output message.</p>"""
    message: "str"
    """<p>The message text associated with the router output message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouterOutputMessage) -> dict:
    out: dict = {}
    out["code"] = value["code"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RouterOutputMessage:
    out: RouterOutputMessage = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        raise DeserializationError("RouterOutputMessage.code required")
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("RouterOutputMessage.message required")
    return out
