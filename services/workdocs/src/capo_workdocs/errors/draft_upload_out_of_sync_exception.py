"""Generated from Smithy shape ``com.amazonaws.workdocs#DraftUploadOutOfSyncException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_workdocs.errors import ServiceError

if TYPE_CHECKING:
    import capo_workdocs.types.error_message_type


class DraftUploadOutOfSyncException_(TypedDict, closed=True):
    message: NotRequired["capo_workdocs.types.error_message_type.ErrorMessageType"]


# --- restJson1 ser/de ---
def serialize_json(value: DraftUploadOutOfSyncException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DraftUploadOutOfSyncException_:
    out: DraftUploadOutOfSyncException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class DraftUploadOutOfSyncException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workdocs#DraftUploadOutOfSyncException``."""

    code: str | None = "DraftUploadOutOfSyncException"

    def __init__(
        self, data: DraftUploadOutOfSyncException_, message: str | None = None
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DraftUploadOutOfSyncException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "DraftUploadOutOfSyncException":
        return cls(deserialize_json(data), message)
