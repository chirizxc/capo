"""Generated from Smithy shape ``com.amazonaws.mediaconvert#TtmlDestinationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min0_max96
    import capo_mediaconvert.types.__integer_min0_max255
    import capo_mediaconvert.types.ttml_background_color
    import capo_mediaconvert.types.ttml_font_color
    import capo_mediaconvert.types.ttml_font_style
    import capo_mediaconvert.types.ttml_font_weight
    import capo_mediaconvert.types.ttml_style_passthrough
    import capo_mediaconvert.types.ttml_text_decoration


class TtmlDestinationSettings(TypedDict, closed=True):
    background_color: NotRequired[
        "capo_mediaconvert.types.ttml_background_color.TtmlBackgroundColor"
    ]
    """Specify the color of the rectangle behind the captions. If Style passthrough is set to enabled, leave blank or set to Auto to pass through the background color from your input captions. If Style passthrough is set to disabled, leave blank or set to Auto to use the default black."""
    background_opacity: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max255.__integerMin0Max255"
    ]
    """Specify the opacity of the background rectangle. Enter a value from 0 to 255, where 0 is transparent and 255 is opaque. If Style passthrough is set to enabled, leave blank to pass through the background style information in your input captions to your output captions. If Style passthrough is set to disabled and backgroundColor is set, leave blank to use a value of 255 (opaque)."""
    font_color: NotRequired["capo_mediaconvert.types.ttml_font_color.TtmlFontColor"]
    """Specify the color of the captions text. If Style passthrough is set to enabled, leave blank or set to Auto to pass through the font color from your input captions. If Style passthrough is set to disabled, leave blank or set to Auto to use the default white."""
    font_opacity: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max255.__integerMin0Max255"
    ]
    """Specify the opacity of the captions. Enter a value from 0 to 255, where 0 is transparent and 255 is opaque. If Style passthrough is set to enabled, leave blank to pass through the font opacity information in your input captions to your output captions. If Style passthrough is set to disabled and fontColor is set, leave blank to use a value of 255 (opaque)."""
    font_size: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max96.__integerMin0Max96"
    ]
    """Specify the Font size in pixels. Must be a positive integer. Set to 0, or leave blank, for automatic font size."""
    font_style: NotRequired["capo_mediaconvert.types.ttml_font_style.TtmlFontStyle"]
    """Specify the font style of the caption text. If Style passthrough is set to enabled, leave blank to pass through the font style from your input captions. If Style passthrough is set to disabled, leave blank to use the default normal style."""
    font_weight: NotRequired["capo_mediaconvert.types.ttml_font_weight.TtmlFontWeight"]
    """Specify the font weight of the caption text. If Style passthrough is set to enabled, leave blank to pass through the font weight from your input captions. If Style passthrough is set to disabled, leave blank to use the default normal weight."""
    style_passthrough: NotRequired[
        "capo_mediaconvert.types.ttml_style_passthrough.TtmlStylePassthrough"
    ]
    """Pass through style and position information from a TTML-like input source (TTML, IMSC, SMPTE-TT) to the TTML output."""
    text_decoration: NotRequired[
        "capo_mediaconvert.types.ttml_text_decoration.TtmlTextDecoration"
    ]
    """Specify the text decoration of the caption text. If Style passthrough is set to enabled, leave blank to pass through the text decoration from your input captions. If Style passthrough is set to disabled, leave blank to use the default of none."""


# --- restJson1 ser/de ---
def serialize_json(value: TtmlDestinationSettings) -> dict:
    out: dict = {}
    if "background_color" in value:
        import capo_mediaconvert.types.ttml_background_color

        out["backgroundColor"] = (
            capo_mediaconvert.types.ttml_background_color.serialize_json(
                value["background_color"]
            )
        )
    if "background_opacity" in value:
        out["backgroundOpacity"] = value["background_opacity"]
    if "font_color" in value:
        import capo_mediaconvert.types.ttml_font_color

        out["fontColor"] = capo_mediaconvert.types.ttml_font_color.serialize_json(
            value["font_color"]
        )
    if "font_opacity" in value:
        out["fontOpacity"] = value["font_opacity"]
    if "font_size" in value:
        out["fontSize"] = value["font_size"]
    if "font_style" in value:
        import capo_mediaconvert.types.ttml_font_style

        out["fontStyle"] = capo_mediaconvert.types.ttml_font_style.serialize_json(
            value["font_style"]
        )
    if "font_weight" in value:
        import capo_mediaconvert.types.ttml_font_weight

        out["fontWeight"] = capo_mediaconvert.types.ttml_font_weight.serialize_json(
            value["font_weight"]
        )
    if "style_passthrough" in value:
        import capo_mediaconvert.types.ttml_style_passthrough

        out["stylePassthrough"] = (
            capo_mediaconvert.types.ttml_style_passthrough.serialize_json(
                value["style_passthrough"]
            )
        )
    if "text_decoration" in value:
        import capo_mediaconvert.types.ttml_text_decoration

        out["textDecoration"] = (
            capo_mediaconvert.types.ttml_text_decoration.serialize_json(
                value["text_decoration"]
            )
        )
    return out


def deserialize_json(data: dict) -> TtmlDestinationSettings:
    out: TtmlDestinationSettings = {}  # type: ignore[typeddict-item]
    if data.get("backgroundColor") is not None:
        import capo_mediaconvert.types.ttml_background_color

        out["background_color"] = (
            capo_mediaconvert.types.ttml_background_color.deserialize_json(
                data["backgroundColor"]
            )
        )
    if data.get("backgroundOpacity") is not None:
        out["background_opacity"] = data["backgroundOpacity"]
    if data.get("fontColor") is not None:
        import capo_mediaconvert.types.ttml_font_color

        out["font_color"] = capo_mediaconvert.types.ttml_font_color.deserialize_json(
            data["fontColor"]
        )
    if data.get("fontOpacity") is not None:
        out["font_opacity"] = data["fontOpacity"]
    if data.get("fontSize") is not None:
        out["font_size"] = data["fontSize"]
    if data.get("fontStyle") is not None:
        import capo_mediaconvert.types.ttml_font_style

        out["font_style"] = capo_mediaconvert.types.ttml_font_style.deserialize_json(
            data["fontStyle"]
        )
    if data.get("fontWeight") is not None:
        import capo_mediaconvert.types.ttml_font_weight

        out["font_weight"] = capo_mediaconvert.types.ttml_font_weight.deserialize_json(
            data["fontWeight"]
        )
    if data.get("stylePassthrough") is not None:
        import capo_mediaconvert.types.ttml_style_passthrough

        out["style_passthrough"] = (
            capo_mediaconvert.types.ttml_style_passthrough.deserialize_json(
                data["stylePassthrough"]
            )
        )
    if data.get("textDecoration") is not None:
        import capo_mediaconvert.types.ttml_text_decoration

        out["text_decoration"] = (
            capo_mediaconvert.types.ttml_text_decoration.deserialize_json(
                data["textDecoration"]
            )
        )
    return out
