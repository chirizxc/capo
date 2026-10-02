"""Generated from Smithy shape ``com.amazonaws.medialive#EmbeddedCaptionPositionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min1_max15


class EmbeddedCaptionPositionSettings(TypedDict, closed=True):
    y_position_line: NotRequired[
        "capo_medialive.types.__integer_min1_max15.__integerMin1Max15"
    ]
    """Specifies the vertical position of the caption as a row counted from the top of the output. Row 1 is the topmost row. Acceptable values are 1 through 15."""


# --- restJson1 ser/de ---
def serialize_json(value: EmbeddedCaptionPositionSettings) -> dict:
    out: dict = {}
    if "y_position_line" in value:
        out["yPositionLine"] = value["y_position_line"]
    return out


def deserialize_json(data: dict) -> EmbeddedCaptionPositionSettings:
    out: EmbeddedCaptionPositionSettings = {}  # type: ignore[typeddict-item]
    if data.get("yPositionLine") is not None:
        out["y_position_line"] = data["yPositionLine"]
    return out
