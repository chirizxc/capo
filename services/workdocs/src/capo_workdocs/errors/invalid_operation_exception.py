"""Generated from Smithy shape ``com.amazonaws.workdocs#InvalidOperationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_workdocs.errors import ServiceError

if TYPE_CHECKING:
    import capo_workdocs.types.error_message_type


class InvalidOperationException_(TypedDict, closed=True):
    message: NotRequired["capo_workdocs.types.error_message_type.ErrorMessageType"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidOperationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidOperationException_:
    out: InvalidOperationException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InvalidOperationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workdocs#InvalidOperationException``."""

    code: str | None = "InvalidOperationException"

    def __init__(self, data: InvalidOperationException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidOperationException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "InvalidOperationException":
        return cls(deserialize_json(data), message)
