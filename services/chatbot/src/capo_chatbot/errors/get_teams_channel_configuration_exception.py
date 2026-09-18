"""Generated from Smithy shape ``com.amazonaws.chatbot#GetTeamsChannelConfigurationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chatbot.errors import ServiceError

if TYPE_CHECKING:
    import capo_chatbot.types.error_message


class GetTeamsChannelConfigurationException_(TypedDict, closed=True):
    message: NotRequired["capo_chatbot.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: GetTeamsChannelConfigurationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> GetTeamsChannelConfigurationException_:
    out: GetTeamsChannelConfigurationException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class GetTeamsChannelConfigurationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chatbot#GetTeamsChannelConfigurationException``."""

    code: str | None = "GetTeamsChannelConfigurationException"

    def __init__(
        self, data: GetTeamsChannelConfigurationException_, message: str | None = None
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="GetTeamsChannelConfigurationException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "GetTeamsChannelConfigurationException":
        return cls(deserialize_json(data), message)
