"""Generated from Smithy shape ``com.amazonaws.quicksight#Palette``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.hex_color


class Palette(TypedDict, closed=True):
    foreground: NotRequired["capo_quicksight.types.hex_color.HexColor"]
    """<p>The foreground color.</p>"""
    background: NotRequired["capo_quicksight.types.hex_color.HexColor"]
    """<p>The background color.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Palette) -> dict:
    out: dict = {}
    if "foreground" in value:
        out["Foreground"] = value["foreground"]
    if "background" in value:
        out["Background"] = value["background"]
    return out


def deserialize_json(data: dict) -> Palette:
    out: Palette = {}  # type: ignore[typeddict-item]
    if data.get("Foreground") is not None:
        out["foreground"] = data["Foreground"]
    if data.get("Background") is not None:
        out["background"] = data["Background"]
    return out
