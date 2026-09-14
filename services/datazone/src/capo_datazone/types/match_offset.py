"""Generated from Smithy shape ``com.amazonaws.datazone#MatchOffset``."""

from typing_extensions import NotRequired, TypedDict


class MatchOffset(TypedDict, closed=True):
    start_offset: NotRequired["int"]
    """<p>The 0-indexed number indicating the start position (inclusive) of a matched term.</p>"""
    end_offset: NotRequired["int"]
    """<p>The 0-indexed number indicating the end position (exclusive) of a matched term.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatchOffset) -> dict:
    out: dict = {}
    if "start_offset" in value:
        out["startOffset"] = value["start_offset"]
    if "end_offset" in value:
        out["endOffset"] = value["end_offset"]
    return out


def deserialize_json(data: dict) -> MatchOffset:
    out: MatchOffset = {}  # type: ignore[typeddict-item]
    if data.get("startOffset") is not None:
        out["start_offset"] = data["startOffset"]
    if data.get("endOffset") is not None:
        out["end_offset"] = data["endOffset"]
    return out
