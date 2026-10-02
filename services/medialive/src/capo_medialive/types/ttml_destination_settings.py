"""Generated from Smithy shape ``com.amazonaws.medialive#TtmlDestinationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.text_caption_position_settings
    import capo_medialive.types.ttml_destination_style_control


class TtmlDestinationSettings(TypedDict, closed=True):
    style_control: NotRequired[
        "capo_medialive.types.ttml_destination_style_control.TtmlDestinationStyleControl"
    ]
    """Controls the source of style and position information for the output captions. PASSTHROUGH - Preserve the style and position from the source captions. USE_CONFIGURED - Don't pass through the style. The output captions will use the default styling. MANUAL - Applies the specified styling and positioning. All other styling and positioning is given default values."""
    position: NotRequired[
        "capo_medialive.types.text_caption_position_settings.TextCaptionPositionSettings"
    ]
    """Specifies the position of the output captions. Applies only when styleControl is set to manual."""


# --- restJson1 ser/de ---
def serialize_json(value: TtmlDestinationSettings) -> dict:
    out: dict = {}
    if "style_control" in value:
        import capo_medialive.types.ttml_destination_style_control

        out["styleControl"] = (
            capo_medialive.types.ttml_destination_style_control.serialize_json(
                value["style_control"]
            )
        )
    if "position" in value:
        import capo_medialive.types.text_caption_position_settings

        out["position"] = (
            capo_medialive.types.text_caption_position_settings.serialize_json(
                value["position"]
            )
        )
    return out


def deserialize_json(data: dict) -> TtmlDestinationSettings:
    out: TtmlDestinationSettings = {}  # type: ignore[typeddict-item]
    if data.get("styleControl") is not None:
        import capo_medialive.types.ttml_destination_style_control

        out["style_control"] = (
            capo_medialive.types.ttml_destination_style_control.deserialize_json(
                data["styleControl"]
            )
        )
    if data.get("position") is not None:
        import capo_medialive.types.text_caption_position_settings

        out["position"] = (
            capo_medialive.types.text_caption_position_settings.deserialize_json(
                data["position"]
            )
        )
    return out
