"""Generated from Smithy shape ``com.amazonaws.quicksight#NegativeFormat``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.limited_string


class NegativeFormat(TypedDict, closed=True):
    prefix: NotRequired["capo_quicksight.types.limited_string.LimitedString"]
    """<p>The prefix for a negative format.</p>"""
    suffix: NotRequired["capo_quicksight.types.limited_string.LimitedString"]
    """<p>The suffix for a negative format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NegativeFormat) -> dict:
    out: dict = {}
    if "prefix" in value:
        out["Prefix"] = value["prefix"]
    if "suffix" in value:
        out["Suffix"] = value["suffix"]
    return out


def deserialize_json(data: dict) -> NegativeFormat:
    out: NegativeFormat = {}  # type: ignore[typeddict-item]
    if data.get("Prefix") is not None:
        out["prefix"] = data["Prefix"]
    if data.get("Suffix") is not None:
        out["suffix"] = data["Suffix"]
    return out
