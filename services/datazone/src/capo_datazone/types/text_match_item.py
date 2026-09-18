"""Generated from Smithy shape ``com.amazonaws.datazone#TextMatchItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.attribute
    import capo_datazone.types.match_offsets


class TextMatchItem(TypedDict, closed=True):
    attribute: NotRequired["capo_datazone.types.attribute.Attribute"]
    """<p>The name of the attribute.</p>"""
    text: NotRequired["str"]
    """<p>Snippet of attribute text containing highlighted content.</p>"""
    match_offsets: NotRequired["capo_datazone.types.match_offsets.MatchOffsets"]
    """<p>List of offsets indicating matching terms in the TextMatchItem text.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextMatchItem) -> dict:
    out: dict = {}
    if "attribute" in value:
        out["attribute"] = value["attribute"]
    if "text" in value:
        out["text"] = value["text"]
    if "match_offsets" in value:
        import capo_datazone.types.match_offsets

        out["matchOffsets"] = capo_datazone.types.match_offsets.serialize_json(
            value["match_offsets"]
        )
    return out


def deserialize_json(data: dict) -> TextMatchItem:
    out: TextMatchItem = {}  # type: ignore[typeddict-item]
    if data.get("attribute") is not None:
        out["attribute"] = data["attribute"]
    if data.get("text") is not None:
        out["text"] = data["text"]
    if data.get("matchOffsets") is not None:
        import capo_datazone.types.match_offsets

        out["match_offsets"] = capo_datazone.types.match_offsets.deserialize_json(
            data["matchOffsets"]
        )
    return out
