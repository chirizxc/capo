"""Generated from Smithy shape ``com.amazonaws.medialive#InputSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.input_codec
    import capo_medialive.types.input_maximum_bitrate
    import capo_medialive.types.input_resolution


class InputSpecification(TypedDict, closed=True):
    codec: NotRequired["capo_medialive.types.input_codec.InputCodec"]
    """Input codec"""
    maximum_bitrate: NotRequired[
        "capo_medialive.types.input_maximum_bitrate.InputMaximumBitrate"
    ]
    """Maximum input bitrate, categorized coarsely"""
    resolution: NotRequired["capo_medialive.types.input_resolution.InputResolution"]
    """Input resolution, categorized coarsely"""


# --- restJson1 ser/de ---
def serialize_json(value: InputSpecification) -> dict:
    out: dict = {}
    if "codec" in value:
        import capo_medialive.types.input_codec

        out["codec"] = capo_medialive.types.input_codec.serialize_json(value["codec"])
    if "maximum_bitrate" in value:
        import capo_medialive.types.input_maximum_bitrate

        out["maximumBitrate"] = (
            capo_medialive.types.input_maximum_bitrate.serialize_json(
                value["maximum_bitrate"]
            )
        )
    if "resolution" in value:
        import capo_medialive.types.input_resolution

        out["resolution"] = capo_medialive.types.input_resolution.serialize_json(
            value["resolution"]
        )
    return out


def deserialize_json(data: dict) -> InputSpecification:
    out: InputSpecification = {}  # type: ignore[typeddict-item]
    if data.get("codec") is not None:
        import capo_medialive.types.input_codec

        out["codec"] = capo_medialive.types.input_codec.deserialize_json(data["codec"])
    if data.get("maximumBitrate") is not None:
        import capo_medialive.types.input_maximum_bitrate

        out["maximum_bitrate"] = (
            capo_medialive.types.input_maximum_bitrate.deserialize_json(
                data["maximumBitrate"]
            )
        )
    if data.get("resolution") is not None:
        import capo_medialive.types.input_resolution

        out["resolution"] = capo_medialive.types.input_resolution.deserialize_json(
            data["resolution"]
        )
    return out
