"""Generated from Smithy shape ``com.amazonaws.medialive#VideoPositionRectangle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min0_max8190
    import capo_medialive.types.__integer_min2_max8192


class VideoPositionRectangle(TypedDict, closed=True):
    height: NotRequired[
        "capo_medialive.types.__integer_min2_max8192.__integerMin2Max8192"
    ]
    """Height in pixels. Must be an even number."""
    width: NotRequired[
        "capo_medialive.types.__integer_min2_max8192.__integerMin2Max8192"
    ]
    """Width in pixels. Must be an even number."""
    x: NotRequired["capo_medialive.types.__integer_min0_max8190.__integerMin0Max8190"]
    """Left offset in pixels. Must be an even number."""
    y: NotRequired["capo_medialive.types.__integer_min0_max8190.__integerMin0Max8190"]
    """Top offset in pixels. Must be an even number."""


# --- restJson1 ser/de ---
def serialize_json(value: VideoPositionRectangle) -> dict:
    out: dict = {}
    if "height" in value:
        out["height"] = value["height"]
    if "width" in value:
        out["width"] = value["width"]
    if "x" in value:
        out["x"] = value["x"]
    if "y" in value:
        out["y"] = value["y"]
    return out


def deserialize_json(data: dict) -> VideoPositionRectangle:
    out: VideoPositionRectangle = {}  # type: ignore[typeddict-item]
    if data.get("height") is not None:
        out["height"] = data["height"]
    if data.get("width") is not None:
        out["width"] = data["width"]
    if data.get("x") is not None:
        out["x"] = data["x"]
    if data.get("y") is not None:
        out["y"] = data["y"]
    return out
