"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#CodeLine``."""

from typing_extensions import NotRequired, TypedDict


class CodeLine(TypedDict, closed=True):
    number: NotRequired["int"]
    """<p>The code line number.</p>"""
    content: NotRequired["str"]
    """<p>The code that contains a vulnerability.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeLine) -> dict:
    out: dict = {}
    if "number" in value:
        out["number"] = value["number"]
    if "content" in value:
        out["content"] = value["content"]
    return out


def deserialize_json(data: dict) -> CodeLine:
    out: CodeLine = {}  # type: ignore[typeddict-item]
    if data.get("number") is not None:
        out["number"] = data["number"]
    if data.get("content") is not None:
        out["content"] = data["content"]
    return out
