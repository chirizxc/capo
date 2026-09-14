"""Generated from Smithy shape ``com.amazonaws.devopsagent#SendMessageTextDelta``."""

from typing_extensions import NotRequired, TypedDict


class SendMessageTextDelta(TypedDict, closed=True):
    text: NotRequired["str"]
    """<p>The text fragment</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendMessageTextDelta) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> SendMessageTextDelta:
    out: SendMessageTextDelta = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    return out
