"""Generated from Smithy shape ``com.amazonaws.medialive#WavSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__double
    import capo_medialive.types.wav_coding_mode


class WavSettings(TypedDict, closed=True):
    bit_depth: NotRequired["capo_medialive.types.__double.__double"]
    """Bits per sample."""
    coding_mode: NotRequired["capo_medialive.types.wav_coding_mode.WavCodingMode"]
    """The audio coding mode for the WAV audio. The mode determines the number of channels in the audio."""
    sample_rate: NotRequired["capo_medialive.types.__double.__double"]
    """Sample rate in Hz."""


# --- restJson1 ser/de ---
def serialize_json(value: WavSettings) -> dict:
    out: dict = {}
    if "bit_depth" in value:
        out["bitDepth"] = (
            "NaN"
            if value["bit_depth"] != value["bit_depth"]
            else "Infinity"
            if value["bit_depth"] == float("inf")
            else "-Infinity"
            if value["bit_depth"] == float("-inf")
            else value["bit_depth"]
        )
    if "coding_mode" in value:
        import capo_medialive.types.wav_coding_mode

        out["codingMode"] = capo_medialive.types.wav_coding_mode.serialize_json(
            value["coding_mode"]
        )
    if "sample_rate" in value:
        out["sampleRate"] = (
            "NaN"
            if value["sample_rate"] != value["sample_rate"]
            else "Infinity"
            if value["sample_rate"] == float("inf")
            else "-Infinity"
            if value["sample_rate"] == float("-inf")
            else value["sample_rate"]
        )
    return out


def deserialize_json(data: dict) -> WavSettings:
    out: WavSettings = {}  # type: ignore[typeddict-item]
    if data.get("bitDepth") is not None:
        out["bit_depth"] = float(data["bitDepth"])
    if data.get("codingMode") is not None:
        import capo_medialive.types.wav_coding_mode

        out["coding_mode"] = capo_medialive.types.wav_coding_mode.deserialize_json(
            data["codingMode"]
        )
    if data.get("sampleRate") is not None:
        out["sample_rate"] = float(data["sampleRate"])
    return out
