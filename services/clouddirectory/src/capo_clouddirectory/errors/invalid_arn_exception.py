"""Generated from Smithy shape ``com.amazonaws.clouddirectory#InvalidArnException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_clouddirectory.errors import ServiceError

if TYPE_CHECKING:
    import capo_clouddirectory.types.exception_message


class InvalidArnException_(TypedDict, closed=True):
    message: NotRequired["capo_clouddirectory.types.exception_message.ExceptionMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidArnException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidArnException_:
    out: InvalidArnException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InvalidArnException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.clouddirectory#InvalidArnException``."""

    code: str | None = "InvalidArnException"

    def __init__(self, data: InvalidArnException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidArnException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict, message: str | None = None) -> "InvalidArnException":
        return cls(deserialize_json(data), message)
