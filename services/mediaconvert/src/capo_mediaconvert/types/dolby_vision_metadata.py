"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DolbyVisionMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer
    import capo_mediaconvert.types.dolby_vision_presence


class DolbyVisionMetadata(TypedDict, closed=True):
    base_layer: NotRequired[
        "capo_mediaconvert.types.dolby_vision_presence.DolbyVisionPresence"
    ]
    """Whether a Dolby Vision component is present in the track."""
    enhancement_layer: NotRequired[
        "capo_mediaconvert.types.dolby_vision_presence.DolbyVisionPresence"
    ]
    """Whether a Dolby Vision component is present in the track."""
    level: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """The Dolby Vision level, which indicates the maximum resolution and frame rate."""
    profile: NotRequired["capo_mediaconvert.types.__integer.__integer"]
    """The Dolby Vision profile, for example 5, 7, or 8. The profile determines the layer structure and playback compatibility of the content."""
    rpu: NotRequired[
        "capo_mediaconvert.types.dolby_vision_presence.DolbyVisionPresence"
    ]
    """Whether a Dolby Vision component is present in the track."""


# --- restJson1 ser/de ---
def serialize_json(value: DolbyVisionMetadata) -> dict:
    out: dict = {}
    if "base_layer" in value:
        import capo_mediaconvert.types.dolby_vision_presence

        out["baseLayer"] = capo_mediaconvert.types.dolby_vision_presence.serialize_json(
            value["base_layer"]
        )
    if "enhancement_layer" in value:
        import capo_mediaconvert.types.dolby_vision_presence

        out["enhancementLayer"] = (
            capo_mediaconvert.types.dolby_vision_presence.serialize_json(
                value["enhancement_layer"]
            )
        )
    if "level" in value:
        out["level"] = value["level"]
    if "profile" in value:
        out["profile"] = value["profile"]
    if "rpu" in value:
        import capo_mediaconvert.types.dolby_vision_presence

        out["rpu"] = capo_mediaconvert.types.dolby_vision_presence.serialize_json(
            value["rpu"]
        )
    return out


def deserialize_json(data: dict) -> DolbyVisionMetadata:
    out: DolbyVisionMetadata = {}  # type: ignore[typeddict-item]
    if data.get("baseLayer") is not None:
        import capo_mediaconvert.types.dolby_vision_presence

        out["base_layer"] = (
            capo_mediaconvert.types.dolby_vision_presence.deserialize_json(
                data["baseLayer"]
            )
        )
    if data.get("enhancementLayer") is not None:
        import capo_mediaconvert.types.dolby_vision_presence

        out["enhancement_layer"] = (
            capo_mediaconvert.types.dolby_vision_presence.deserialize_json(
                data["enhancementLayer"]
            )
        )
    if data.get("level") is not None:
        out["level"] = data["level"]
    if data.get("profile") is not None:
        out["profile"] = data["profile"]
    if data.get("rpu") is not None:
        import capo_mediaconvert.types.dolby_vision_presence

        out["rpu"] = capo_mediaconvert.types.dolby_vision_presence.deserialize_json(
            data["rpu"]
        )
    return out
