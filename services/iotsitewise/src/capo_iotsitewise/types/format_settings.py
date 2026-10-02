"""Generated from Smithy shape ``com.amazonaws.iotsitewise#FormatSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.positive_integer


class FormatSettings(TypedDict, closed=True):
    frames_per_second: NotRequired[
        "capo_iotsitewise.types.positive_integer.PositiveInteger"
    ]
    """<p>The target frame rate for the output.</p>"""
    width_in_pixels: NotRequired[
        "capo_iotsitewise.types.positive_integer.PositiveInteger"
    ]
    """<p>The target width of the output, in pixels.</p>"""
    height_in_pixels: NotRequired[
        "capo_iotsitewise.types.positive_integer.PositiveInteger"
    ]
    """<p>The target height of the output, in pixels.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormatSettings) -> dict:
    out: dict = {}
    if "frames_per_second" in value:
        out["framesPerSecond"] = value["frames_per_second"]
    if "width_in_pixels" in value:
        out["widthInPixels"] = value["width_in_pixels"]
    if "height_in_pixels" in value:
        out["heightInPixels"] = value["height_in_pixels"]
    return out


def deserialize_json(data: dict) -> FormatSettings:
    out: FormatSettings = {}  # type: ignore[typeddict-item]
    if data.get("framesPerSecond") is not None:
        out["frames_per_second"] = data["framesPerSecond"]
    if data.get("widthInPixels") is not None:
        out["width_in_pixels"] = data["widthInPixels"]
    if data.get("heightInPixels") is not None:
        out["height_in_pixels"] = data["heightInPixels"]
    return out
