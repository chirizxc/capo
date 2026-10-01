"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AspectRatio``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer


class AspectRatio(TypedDict, closed=True):
    denominator: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """The denominator, or bottom number, in the fractional aspect ratio. For example, for a display aspect ratio of 16 / 9, the denominator would be 9."""
    numerator: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """The numerator, or top number, in the fractional aspect ratio. For example, for a display aspect ratio of 16 / 9, the numerator would be 16."""


# --- restJson1 ser/de ---
def serialize_json(value: AspectRatio) -> dict:
    out: dict = {}
    if "denominator" in value:
        out["denominator"] = value["denominator"]
    if "numerator" in value:
        out["numerator"] = value["numerator"]
    return out


def deserialize_json(data: dict) -> AspectRatio:
    out: AspectRatio = {}  # type: ignore[typeddict-item]
    if data.get("denominator") is not None:
        out["denominator"] = data["denominator"]
    if data.get("numerator") is not None:
        out["numerator"] = data["numerator"]
    return out
