"""Generated from Smithy shape ``com.amazonaws.pinpoint#VoiceChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__boolean


class VoiceChannelRequest(TypedDict, closed=True):
    enabled: NotRequired["capo_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether to enable the voice channel for the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VoiceChannelRequest) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> VoiceChannelRequest:
    out: VoiceChannelRequest = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    return out
