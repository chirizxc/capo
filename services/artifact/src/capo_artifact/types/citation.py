"""Generated from Smithy shape ``com.amazonaws.artifact#Citation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_artifact.types.long_string_attribute
    import capo_artifact.types.short_string_attribute


class Citation(TypedDict, closed=True):
    source_label: NotRequired[
        "capo_artifact.types.short_string_attribute.ShortStringAttribute"
    ]
    """<p>Label identifying the compliance source.</p>"""
    source_content: NotRequired[
        "capo_artifact.types.long_string_attribute.LongStringAttribute"
    ]
    """<p>Content text from the compliance source.</p>"""
    source_link: NotRequired[
        "capo_artifact.types.long_string_attribute.LongStringAttribute"
    ]
    """<p>Link to the compliance source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Citation) -> dict:
    out: dict = {}
    if "source_label" in value:
        out["sourceLabel"] = value["source_label"]
    if "source_content" in value:
        out["sourceContent"] = value["source_content"]
    if "source_link" in value:
        out["sourceLink"] = value["source_link"]
    return out


def deserialize_json(data: dict) -> Citation:
    out: Citation = {}  # type: ignore[typeddict-item]
    if data.get("sourceLabel") is not None:
        out["source_label"] = data["sourceLabel"]
    if data.get("sourceContent") is not None:
        out["source_content"] = data["sourceContent"]
    if data.get("sourceLink") is not None:
        out["source_link"] = data["sourceLink"]
    return out
