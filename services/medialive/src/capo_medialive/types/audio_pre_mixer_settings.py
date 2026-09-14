"""Generated from Smithy shape ``com.amazonaws.medialive#AudioPreMixerSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__double_min_negative60_max60
    import capo_medialive.types.__integer_min1_max16
    import capo_medialive.types.audio_normalization_settings
    import capo_medialive.types.remix_settings


class AudioPreMixerSettings(TypedDict, closed=True):
    audio_normalization_settings: NotRequired[
        "capo_medialive.types.audio_normalization_settings.AudioNormalizationSettings"
    ]
    """Audio normalization settings for loudness control. When specified, audio loudness will be normalized according to the chosen algorithm."""
    channels: NotRequired[
        "capo_medialive.types.__integer_min1_max16.__integerMin1Max16"
    ]
    """Number of audio channels. If specified, the audio will be remixed to match this channel count. Ignored if remixSettings is specified."""
    gain_db: NotRequired[
        "capo_medialive.types.__double_min_negative60_max60.__doubleMinNegative60Max60"
    ]
    """Gain adjustment in dB to apply. Range: -60 to +60 dB"""
    remix_settings: NotRequired["capo_medialive.types.remix_settings.RemixSettings"]
    """Settings that control how input audio channels are remixed. When specified, allows fine-grained control over channel mapping and gain levels. Takes precedence over the 'channels' setting."""


# --- restJson1 ser/de ---
def serialize_json(value: AudioPreMixerSettings) -> dict:
    out: dict = {}
    if "audio_normalization_settings" in value:
        import capo_medialive.types.audio_normalization_settings

        out["audioNormalizationSettings"] = (
            capo_medialive.types.audio_normalization_settings.serialize_json(
                value["audio_normalization_settings"]
            )
        )
    if "channels" in value:
        out["channels"] = value["channels"]
    if "gain_db" in value:
        out["gainDb"] = (
            "NaN"
            if value["gain_db"] != value["gain_db"]
            else "Infinity"
            if value["gain_db"] == float("inf")
            else "-Infinity"
            if value["gain_db"] == float("-inf")
            else value["gain_db"]
        )
    if "remix_settings" in value:
        import capo_medialive.types.remix_settings

        out["remixSettings"] = capo_medialive.types.remix_settings.serialize_json(
            value["remix_settings"]
        )
    return out


def deserialize_json(data: dict) -> AudioPreMixerSettings:
    out: AudioPreMixerSettings = {}  # type: ignore[typeddict-item]
    if data.get("audioNormalizationSettings") is not None:
        import capo_medialive.types.audio_normalization_settings

        out["audio_normalization_settings"] = (
            capo_medialive.types.audio_normalization_settings.deserialize_json(
                data["audioNormalizationSettings"]
            )
        )
    if data.get("channels") is not None:
        out["channels"] = data["channels"]
    if data.get("gainDb") is not None:
        out["gain_db"] = float(data["gainDb"])
    if data.get("remixSettings") is not None:
        import capo_medialive.types.remix_settings

        out["remix_settings"] = capo_medialive.types.remix_settings.deserialize_json(
            data["remixSettings"]
        )
    return out
