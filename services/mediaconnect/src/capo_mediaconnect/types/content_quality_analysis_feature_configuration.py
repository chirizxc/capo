"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ContentQualityAnalysisFeatureConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.black_frames_configuration
    import capo_mediaconnect.types.frozen_frames_configuration
    import capo_mediaconnect.types.silent_audio_configuration


class ContentQualityAnalysisFeatureConfiguration(TypedDict, closed=True):
    black_frames: NotRequired[
        "capo_mediaconnect.types.black_frames_configuration.BlackFramesConfiguration"
    ]
    """<p>Settings for black frames detection.</p>"""
    frozen_frames: NotRequired[
        "capo_mediaconnect.types.frozen_frames_configuration.FrozenFramesConfiguration"
    ]
    """<p>Settings for frozen frames detection.</p>"""
    silent_audio: NotRequired[
        "capo_mediaconnect.types.silent_audio_configuration.SilentAudioConfiguration"
    ]
    """<p>Settings for silent audio detection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentQualityAnalysisFeatureConfiguration) -> dict:
    out: dict = {}
    if "black_frames" in value:
        import capo_mediaconnect.types.black_frames_configuration

        out["blackFrames"] = (
            capo_mediaconnect.types.black_frames_configuration.serialize_json(
                value["black_frames"]
            )
        )
    if "frozen_frames" in value:
        import capo_mediaconnect.types.frozen_frames_configuration

        out["frozenFrames"] = (
            capo_mediaconnect.types.frozen_frames_configuration.serialize_json(
                value["frozen_frames"]
            )
        )
    if "silent_audio" in value:
        import capo_mediaconnect.types.silent_audio_configuration

        out["silentAudio"] = (
            capo_mediaconnect.types.silent_audio_configuration.serialize_json(
                value["silent_audio"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContentQualityAnalysisFeatureConfiguration:
    out: ContentQualityAnalysisFeatureConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("blackFrames") is not None:
        import capo_mediaconnect.types.black_frames_configuration

        out["black_frames"] = (
            capo_mediaconnect.types.black_frames_configuration.deserialize_json(
                data["blackFrames"]
            )
        )
    if data.get("frozenFrames") is not None:
        import capo_mediaconnect.types.frozen_frames_configuration

        out["frozen_frames"] = (
            capo_mediaconnect.types.frozen_frames_configuration.deserialize_json(
                data["frozenFrames"]
            )
        )
    if data.get("silentAudio") is not None:
        import capo_mediaconnect.types.silent_audio_configuration

        out["silent_audio"] = (
            capo_mediaconnect.types.silent_audio_configuration.deserialize_json(
                data["silentAudio"]
            )
        )
    return out
