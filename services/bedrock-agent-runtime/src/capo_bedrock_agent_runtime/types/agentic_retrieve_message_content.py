"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveMessageContent``."""

from typing_extensions import NotRequired, TypedDict


class AgenticRetrieveMessageContent(TypedDict, closed=True):
    text: NotRequired["str"]
    """<p>The text content of the message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveMessageContent) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> AgenticRetrieveMessageContent:
    out: AgenticRetrieveMessageContent = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    return out
