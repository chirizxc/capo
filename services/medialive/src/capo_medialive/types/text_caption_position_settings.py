"""Generated from Smithy shape ``com.amazonaws.medialive#TextCaptionPositionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min0_max100


class TextCaptionPositionSettings(TypedDict, closed=True):
    y_position_percentage: NotRequired[
        "capo_medialive.types.__integer_min0_max100.__integerMin0Max100"
    ]
    """Specifies the vertical position of the top edge of the caption relative to the top of the output as a percentage. A value of 0 places the caption at the top of the output and 100 at the bottom."""


# --- restJson1 ser/de ---
def serialize_json(value: TextCaptionPositionSettings) -> dict:
    out: dict = {}
    if "y_position_percentage" in value:
        out["yPositionPercentage"] = value["y_position_percentage"]
    return out


def deserialize_json(data: dict) -> TextCaptionPositionSettings:
    out: TextCaptionPositionSettings = {}  # type: ignore[typeddict-item]
    if data.get("yPositionPercentage") is not None:
        out["y_position_percentage"] = data["yPositionPercentage"]
    return out
