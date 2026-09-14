"""Generated from Smithy shape ``com.amazonaws.sagemakerjobruntime#AccessDeniedException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sagemakerjobruntime.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_sagemakerjobruntime.types.failure_reason


class AccessDeniedException_(TypedDict, closed=True):
    message: "capo_sagemakerjobruntime.types.failure_reason.FailureReason"


# --- restJson1 ser/de ---
def serialize_json(value: AccessDeniedException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("AccessDeniedException_.message required")
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sagemakerjobruntime#AccessDeniedException``."""

    code: str | None = "AccessDeniedException"

    def __init__(self, data: AccessDeniedException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccessDeniedException",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "AccessDeniedException":
        return cls(deserialize_json(data), message)
