"""Generated from Smithy shape ``com.amazonaws.qconnect#Highlight``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.highlight_offset


class Highlight(TypedDict, closed=True):
    begin_offset_inclusive: "capo_qconnect.types.highlight_offset.HighlightOffset"
    """<p>The offset for the start of the highlight.</p>"""
    end_offset_exclusive: "capo_qconnect.types.highlight_offset.HighlightOffset"
    """<p>The offset for the end of the highlight.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Highlight) -> dict:
    out: dict = {}
    out["beginOffsetInclusive"] = value.get("begin_offset_inclusive", 0)
    out["endOffsetExclusive"] = value.get("end_offset_exclusive", 0)
    return out


def deserialize_json(data: dict) -> Highlight:
    out: Highlight = {}  # type: ignore[typeddict-item]
    if data.get("beginOffsetInclusive") is not None:
        out["begin_offset_inclusive"] = data["beginOffsetInclusive"]
    else:
        out["begin_offset_inclusive"] = 0
    if data.get("endOffsetExclusive") is not None:
        out["end_offset_exclusive"] = data["endOffsetExclusive"]
    else:
        out["end_offset_exclusive"] = 0
    return out
