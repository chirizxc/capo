"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SpeakerDiarizationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.enabled


class SpeakerDiarizationSettings(TypedDict, closed=True):
    enabled: "capo_lex_models_v2.types.enabled.Enabled"
    """<p>Specifies whether speaker diarization is enabled for the bot locale. Set to <code>true</code> to have Amazon Lex treat speech from speakers other than the primary speaker as non-speech. Set to <code>false</code> to disable speaker diarization and rely on voice activity detection alone.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpeakerDiarizationSettings) -> dict:
    out: dict = {}
    out["enabled"] = value.get("enabled", False)
    return out


def deserialize_json(data: dict) -> SpeakerDiarizationSettings:
    out: SpeakerDiarizationSettings = {}  # type: ignore[typeddict-item]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    return out
