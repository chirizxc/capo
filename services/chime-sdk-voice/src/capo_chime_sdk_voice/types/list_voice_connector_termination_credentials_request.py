"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ListVoiceConnectorTerminationCredentialsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.voice_connector_id


class ListVoiceConnectorTerminationCredentialsRequest(TypedDict, closed=True):
    voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId"
    """<p>The Voice Connector ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVoiceConnectorTerminationCredentialsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListVoiceConnectorTerminationCredentialsRequest:
    out: ListVoiceConnectorTerminationCredentialsRequest = {}  # type: ignore[typeddict-item]
    return out
